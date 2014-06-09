#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from urllib import urlopen
from xml.etree import ElementTree
from datetime import datetime
import time
import json

con = lite.connect('changesets.sqlite')
geojson = '{ "type": "FeatureCollection", "features": [ ' #] }

f = open('myfile.js','w')
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
    ways = tree.findall("create/way")
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



with con:
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM osm_changeset")

    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break

        get_data(row[0])

        #print len(geojson["features"])

#json.dump(geojson, open('aude.js', 'w'))
f.close()
print 'saving geojson'

