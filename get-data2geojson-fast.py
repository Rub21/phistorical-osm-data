#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
from urllib import urlopen
from xml.etree import ElementTree
from datetime import datetime
import time
import json
from shapely.geometry import box, Point
import timeit
import threading

if (len(sys.argv) < 5):
    raise 'Ejecutar: get-data2geojson minx, miny, maxx, maxy, user'

minx = float(sys.argv[1])
miny = float(sys.argv[2])
maxx = float(sys.argv[3])
maxy = float(sys.argv[4])
user = sys.argv[5]


#connecion a base de datos
con = lite.connect('get_changesets/changesets.sqlite')

#inicializamos el geojson
geojson = '{ "type": "FeatureCollection", "features": ['

#Generar dos Archivos un de Ways y otro de Points
file_ways = open(user + '-ways-fast.geojson','w')
file_ways.write(geojson)

file_nodes = open(user + '-nodes-fast.geojson','w')
file_nodes.write(geojson)



#optiene el historial de un nodo, 
def get_node_history(id):
    url = 'https://www.openstreetmap.org/api/0.6/node/%s/history' %(id)
    print url
    tree = ElementTree.parse(urlopen(url))
    nodes = tree.findall("node")
    visible_version=[]
    visible_version.append(nodes[len(nodes)-1].attrib['visible'])
    visible_version.append(nodes[len(nodes)-1].attrib['version'])
    return visible_version

#optiene el historial de un way,     
def get_way_history(id):
    url = 'https://www.openstreetmap.org/api/0.6/way/%s/history' %(id)
    print url
    tree = ElementTree.parse(urlopen(url))
    ways = tree.findall("way")
    visible_version=[]
    visible_version.append(ways[len(ways)-1].attrib['visible'])
    visible_version.append(ways[len(ways)-1].attrib['version'])
    return visible_version

def get_data(id):
    url = 'http://www.openstreetmap.org/api/0.6/changeset/%s/download' %(id)
    print url
    tree = ElementTree.parse(urlopen(url))
    geojson = { "type": "FeatureCollection", "features": [] }

    nodes_created = tree.findall("create/node")
    nodes_modif = tree.findall("modify/node")
    nodes = list(set(nodes_created + nodes_modif))

    ways_created = tree.findall("create/way")
    ways_modif = tree.findall("modify/way")
    ways = list(set(ways_created + ways_modif))
    #ways = tree.findall(".//tag[@k='building']")

    nodeidx = {}
    for n in nodes:
        nodeidx[n.attrib['id']] = [float(n.attrib['lon']), float(n.attrib['lat'])]
        tags = {}
        for p in n.iterfind('tag'):
            tags[p.attrib['k']] = p.attrib['v']

        if len(tags)>0:
            #print tags
            node = {
                "type": "Feature",
                "geometry": {
                "type": 'Point',
                "coordinates": [0,0]
                },
                    "properties": {}
            }
            
            node['properties']['id'] = n.attrib['id']
            vis_ver=get_node_history(n.attrib['id']) #optiene version y visible en un nodo

            node['properties']['visible'] = vis_ver[0]
            node['properties']['version'] = int(vis_ver[1])
            
            if tags.has_key('addr:housenumber'):
                node['properties']['adrr'] = 'yes'
                node['geometry']['coordinates']=nodeidx[n.attrib['id']]
                json.dump(node,file_nodes)
                file_nodes.write(',')

            else:
                node['properties']['poi'] = 'yes'
                node['geometry']['coordinates']=nodeidx[n.attrib['id']]
                #json.dump(node,file_nodes)
                #file_nodes.write(',')
                file_nodes.write(json.dumps(node)+',')

    #print 'mapping ways'

    for w in ways:
        tags = {}
        for t in w.iterfind('tag'):
            tags[t.attrib['k']] = t.attrib['v']
        way = {
            "type": "Feature",
            "geometry": {
                "type": 'LineString',
                "coordinates": []
            },
            "properties": { }
            }
        way['properties']['id'] = w.attrib['id']

        if tags.has_key('building'):
            for n in w.iterfind('nd'):
            	if n.attrib['ref'] in nodeidx:
            		way['geometry']['coordinates'].append(nodeidx[n.attrib['ref']])

            vis_ver=get_way_history(w.attrib['id']) #optiene version y visible en un way
            way['properties']['visible'] = vis_ver[0]
            way['properties']['version'] = int(vis_ver[1])
            #json.dump(way,file_ways)
            file_ways.write(json.dumps(way)+',')
            #file_ways.write(',')




     		
def startThreads():
	bbox = box(minx, miny, maxx, maxy)
	#(minx, miny, maxx, maxy
	with con:
	    
	    cur = con.cursor()
        sql = "SELECT * FROM osm_changeset where osm_user='%s';" % (user)
        cur.execute(sql)
        while True:
	        row = cur.fetchone()
	        if row == None:
	            break
	        lat = (row[4] + row[6])/2
	        lon = (row[3] + row[5])/2
	        point = Point(lat, lon)

	        if bbox.contains(point): #polygon.contains(point)
	            threat=threading.Thread(target=get_data, args=(row[0],))
	            threat.start()
	            #threat.join()




#MAIN
#inicio de tiempo
tic=timeit.default_timer()


#iniciamos a ejecutar lo hilos
startThreads()

#file_ways.write('{ "type": "Feature", "geometry": { "type": "LineString", "coordinates": [] }, "properties": { } }]}')
#file_ways.close()

#file_nodes.write('{ "type": "Feature", "geometry": { "type": "Point", "coordinates": [] }, "properties": { } }]}')
#file_nodes.close()
toc=timeit.default_timer()
print 'saving geojson and take %s min' %((toc - tic)/60)