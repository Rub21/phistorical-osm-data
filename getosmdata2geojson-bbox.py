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
geojson = '{ "type": "FeatureCollection", "features": [ ' #] }

f = open('aude2.geojson','w')
f.write(geojson)

def get_data(id):
    url = 'http://www.openstreetmap.org/api/0.6/changeset/%s/download' %(id)
    print url
    tree = ElementTree.parse(urlopen(url))
    geojson = { "type": "FeatureCollection", "features": [] }

    nodes_created = tree.findall("create/node")
    nodes_modif = tree.findall("modify/node")
    nodes = list(set(nodes_created + nodes_modif))

    #print type(nodes)
    #print len(nodes)
    ways_created = tree.findall("create/way")
    ways_modif = tree.findall("modify/way")
    ways = list(set(ways_created + ways_modif))
    #print len(ways)

    nodeidx = {}

    
    #print 'mapping nodes'

    for n in nodes:
        nodeidx[n.attrib['id']] = [float(n.attrib['lon']), float(n.attrib['lat'])]

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
	       	#way['properties']['building'] = tags['building']
            #geojson['features'].append(way)
            json.dump(way,f)
            f.write(',')


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
f.write('{ "type": "Feature", "geometry": { "type": "LineString", "coordinates": [] }, "properties": { } }]}')
f.close()
print 'saving geojson'

