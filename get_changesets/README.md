# Optener los datos Latest Weekly Changesets

http://planet.openstreetmap.org/?
http://planet.openstreetmap.org/planet/changesets-latest.osm.bz2


# Optener changessets por usuario

Basado en https://github.com/tmcw/sometimemachine

ejecutar para crear la base de datos

	cat schema.sql | sqlite3 changesets.sqlite


ejecutar para optener los canbios de un usuario example: OSM user = Rub21:

	python GetChangeset_byuser2sqlite.py changesets-latest.osm changesets.sqlite Rub21

