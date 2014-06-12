PHistorical-osm-data
====================
Primero ejecutar : https://github.com/Rub21/PHistorical-osm-data/tree/master/get_changesets

Para optener los cambio ejecutar:

Bbox para NY: 40.495298,-74.234619,40.998849,-73.330994
	
	python get-data2geojson.py 40.495298 -74.234619 40.998849 -73.330994 Rub21

`get-data2geojson.py` optendra los todos los cambio que se ralizado por el usario Rub21
	

ejemplo: 
	- Nuevos nodes, y ways
	- Cuales de los nodos y ways que el usuario Rub21 a editado fueron removidos por otro usurios
	- Cules de los nodes y  ways que el usuario Rub21  a editdo fureon editados despues por otros usuarios
	-(sim implementar): Que nodeos y wyas fueron eliminados por el usuario Rub21

get-data2geojson.py, esta implementado para que se ejecute secuencialmente, podria tomar varios minutos optener todos los datos de un usuario:


si es que decea optener de manera mas rapide ls datos podria ejecutar: esto trabaja atraves de hilos de python aun falta afinar para que funcione al 100%


