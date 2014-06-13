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
import time


#optiene el historial de un nodo, 
def get_node_history(id):
    url = 'https://www.openstreetmap.org/api/0.6/node/%s/history' %(id)
    tree = ElementTree.parse(urlopen(url))
    nodes = tree.findall("node")
    visible_version=[]
    visible_version.append(nodes[len(nodes)-1].attrib['visible'])
    visible_version.append(nodes[len(nodes)-1].attrib['version'])
    return visible_version


#optiene el historial de un way, 
def get_way_history(id):
    url = 'https://www.openstreetmap.org/api/0.6/way/%s/history' %(id)
    tree = ElementTree.parse(urlopen(url))
    ways = tree.findall("way")
    visible_version=[]
    visible_version.append(ways[len(ways)-1].attrib['visible'])
    visible_version.append(ways[len(ways)-1].attrib['version'])
    return visible_version


    
def worker():
    print threading.currentThread().getName(), ‘Lanzado’
    time.sleep(2)
    print threading.currentThread().getName(), ‘Deteniendo’

def servicio():
    print threading.currentThread().getName(), ‘Lanzado’
    print threading.currentThread().getName(), ‘Deteniendo’

t = threading.Thread(target=servicio, name=‘Servicio’)

w = threading.Thread(target=worker, name=‘Worker’)

z = threading.Thread(target=worker)

w.start()

z.start()

t.start()

