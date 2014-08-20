#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from urllib import urlopen
from xml.etree import ElementTree
from datetime import datetime
import time
import json
import timeit
import threading

#connecion a base de datos


con = lite.connect('get_changesets/changesets.sqlite', check_same_thread=False)
#con = lite.connect('changesets.sqlite', check_same_thread=False)
c = con.cursor()
cur = con.cursor()

cur.execute("""PRAGMA synchronous=0""")
cur.execute("""PRAGMA locking_mode=EXCLUSIVE""")
cur.execute("""PRAGMA journal_mode=DELETE""")

#Crear tablas en la base de datos
table_nodes ="create table %s (%s integer PRIMARY KEY, %s text , %s integer)" % ("nodes","id","visible","version")
table_ways ="create table %s (%s integer PRIMARY KEY, %s text , %s integer)" % ("ways","id","visible","version")
table_relations ="create table %s (%s integer PRIMARY KEY, %s text , %s integer)" % ("relations","id","visible","version")
print table_nodes
c.execute(table_nodes)
c.execute(table_ways)
c.execute(table_relations)



#querys para ingresar datos
query_nodes = """insert into nodes(id,visible,version) values (?, ?, ?)"""
query_ways = """insert into ways(id,visible,version) values (?, ?, ?)"""
query_relations = """insert into relations(id,visible,version) values (?, ?, ?)"""

user = sys.argv[1]

#optiene el historial de un nodo, 
def get_node_history(id):
    url = 'https://www.openstreetmap.org/api/0.6/node/%s/history' %(id)
    print url
    tree = ElementTree.parse(urlopen(url))
    nodes = tree.findall("node")
    visible_version_user=[]
    visible_version_user.append(nodes[len(nodes)-1].attrib['visible'])
    visible_version_user.append(nodes[len(nodes)-1].attrib['version'])
    #visible_version_user.append(nodes[len(nodes)-1].attrib['user'])
    #print nodes[len(nodes)-1].attrib['user']
    return visible_version_user

#optiene el historial de un way,     
def get_way_history(id):
    url = 'https://www.openstreetmap.org/api/0.6/way/%s/history' %(id)
    print url
    tree = ElementTree.parse(urlopen(url))
    ways = tree.findall("way")
    visible_version_user=[]
    visible_version_user.append(ways[len(ways)-1].attrib['visible'])
    visible_version_user.append(ways[len(ways)-1].attrib['version'])
    #visible_version_user.append(ways[len(ways)-1].attrib['user'])
    #print ways[len(ways)-1].attrib['user']
    return visible_version_user
#optiene el historial de un way,     
def get_relation_history(id):
    url = 'https://www.openstreetmap.org/api/0.6/relation/%s/history' %(id)
    print url
    tree = ElementTree.parse(urlopen(url))
    ways = tree.findall("relation")
    visible_version_user=[]
    visible_version_user.append(ways[len(ways)-1].attrib['visible'])
    visible_version_user.append(ways[len(ways)-1].attrib['version'])
    #visible_version_user.append(ways[len(ways)-1].attrib['user'])
    #print ways[len(ways)-1].attrib['user']
    return visible_version_user

def get_data(id):
    url = 'http://www.openstreetmap.org/api/0.6/changeset/%s/download' %(id)
    print url
    tree = ElementTree.parse(urlopen(url))
    #optenemos nodos creados y modificados
    nodes_created = tree.findall("create/node")
    nodes_modif = tree.findall("modify/node")
    nodes = list(set(nodes_created + nodes_modif))
     #optenemos ways creados y modificados
    ways_created = tree.findall("create/way")
    ways_modif = tree.findall("modify/way")
    ways = list(set(ways_created + ways_modif))
    #optenemos relaciones creados y modificados
    relations_created = tree.findall("create/relation")
    relations_modif = tree.findall("modify/relation")
    relations = list(set(relations_created + relations_modif))

    #procesando lo nodos
    for n in nodes:
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
                    "properties": {}
            }
            node['properties']['id'] = n.attrib['id']

            visible_version_user=get_node_history(n.attrib['id']) #optiene version y visible en un nodo
            node['properties']['visible'] = visible_version_user[0]
            node['properties']['version'] = int(visible_version_user[1])
            #node['properties']['user'] = visible_version_user[2]
            #print node
            try:
                c.execute(query_nodes,(int(node['properties']['id']),  node['properties']['visible'],int(node['properties']['version'])))
                con.commit()
            except: 
                pass

    for w in ways:
        tags = {}
        for t in w.iterfind('tag'):
            tags[t.attrib['k']] = t.attrib['v']

        if len(tags)>0:
            way = {
                "type": "Feature",
                "geometry": {
                    "type": 'LineString',
                    "coordinates": []
                },
                "properties": { }
                }
            way['properties']['id'] = w.attrib['id']

            visible_version_user=get_way_history(w.attrib['id']) #optiene version y visible en un way
            way['properties']['visible'] = visible_version_user[0]
            way['properties']['version'] = int(visible_version_user[1])
            #way['properties']['user'] = visible_version_user[2]
            #print way
            try:
                c.execute(query_ways,(int(way['properties']['id']),  way['properties']['visible'],int(way['properties']['version'])))
                con.commit()
            except: 
                pass

    for r in relations:
        tags = {}
        for t in r.iterfind('tag'):
            tags[t.attrib['k']] = t.attrib['v']

        if len(tags)>0:
            relation = {
                "type": "Feature",
                "geometry": {
                    "type": 'LineString',
                    "coordinates": []
                },
                "properties": { }
                }
            relation['properties']['id'] = r.attrib['id']
            visible_version_user=get_relation_history(r.attrib['id']) #optiene version y visible en un way
            relation['properties']['visible'] = visible_version_user[0]
            relation['properties']['version'] = int(visible_version_user[1])
            #relation['properties']['user'] = visible_version_user[2]
            try:
                c.execute(query_relations,(int(relation['properties']['id']),  relation['properties']['visible'],int(relation['properties']['version'])))
                con.commit()
            except: 
                pass



#inicio de tiempo
tic=timeit.default_timer()


with con:
    cur = con.cursor()  
    sql = "SELECT changeset_id FROM osm_changeset WHERE osm_user='%s' ORDER BY changeset_id DESC;" % (user)
    cur.execute(sql)

    while True:
        row = cur.fetchone()
        print row
        if row == None:
           # print "columna none"
            break

        print "=================================================== : %s"%(row[0])
        get_data(row[0])



#tiempo que tomo
toc=timeit.default_timer()
print 'saving geojson and take %s min' %((toc - tic)/60)