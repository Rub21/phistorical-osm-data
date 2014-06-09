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

con = lite.connect('changesets.sqlite')

#inicializamos el geojson
geojson = '{ "type": "FeatureCollection", "features": [ ' #] }

#Generar dor Archivos un de Ways y otro de Points
file_ways = open('ways.geojson','w')
file_ways.write(geojson)

file_nodes = open('nodes.geojson','w')
file_nodes.write(geojson)


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

    nodeidx = {}

    for n in nodes:
        nodeidx[n.attrib['id']] = [float(n.attrib['lon']), float(n.attrib['lat'])]

        tags = {}
        for p in n.iterfind('tag'):
            tags[p.attrib['k']] = p.attrib['v']

        if len(tags)>0:
            node = {
                "type": "Feature",
                "geometry": {
                "type": 'Point',
                "coordinates": [0,0]
                },
                    "properties": { }
            }

            node['properties']['v'] = int(n.attrib['version'])

            if tags.has_key('addr:housenumber'):
                node['properties']['adrr'] = 'yes'
                node['geometry']['coordinates']=nodeidx[n.attrib['id']]
                json.dump(node,file_nodes)
                file_nodes.write(',')

            else:
                node['properties']['poi'] = 'yes'
                node['geometry']['coordinates']=nodeidx[n.attrib['id']]
                json.dump(node,file_nodes)
                file_nodes.write(',')

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

        if tags.has_key('building'):
            for n in w.iterfind('nd'):
            	if n.attrib['ref'] in nodeidx:
            		way['geometry']['coordinates'].append(nodeidx[n.attrib['ref']])
            way['properties']['v'] = int(w.attrib['version'])
	       	#way['properties']['building'] = tags['building']
            #geojson['features'].append(way)
            json.dump(way,file_ways)
            file_ways.write(',')


bbox = box(40.495298,-74.234619,40.998849,-73.330994)
#(minx, miny, maxx, maxy
with con:
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM osm_changeset")

    while True:
        row = cur.fetchone()
        if row == None:
            break
        lat = (row[4] + row[6])/2
        lon = (row[3] + row[5])/2
        point = Point(lat, lon)

        if bbox.contains(point): #polygon.contains(point)
            get_data(row[0])


file_ways.write('{ "type": "Feature", "geometry": { "type": "LineString", "coordinates": [] }, "properties": { } }]}')
file_ways.close()

file_nodes.write('{ "type": "Feature", "geometry": { "type": "Point", "coordinates": [] }, "properties": { } }]}')
file_nodes.close()
print 'saving geojson'

