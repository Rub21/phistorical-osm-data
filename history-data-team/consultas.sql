DELETE FROM osm_changeset WHERE osm_user = 'Luis36995';



SELECT SUM(num_changes) FROM osm_changeset WHERE osm_user='Rub21'

4,538,100



SELECT SUM(num_changes) FROM osm_changeset WHERE osm_user='ediyes'

1,721,763

SELECT SUM(num_changes) FROM osm_changeset WHERE osm_user='Luis36995'

1,100,311

SELECT SUM(num_changes) FROM osm_changeset WHERE osm_user='dannykath'

46,179


SELECT SUM(num_changes) FROM osm_changeset WHERE osm_user='RichRico'

63,184


-----Resultados por mes

SELECT  sum(num_changes) ,substr( datetime(closed_at, 'unixepoch'),0,8)  FROM osm_changeset WHERE osm_user='ediyes'   group by substr( datetime(closed_at, 'unixepoch'),0,8)  order by substr( datetime(closed_at, 'unixepoch'),0,8)  
"2011-08","11145"
"2011-09","12274"
"2011-10","538"
"2012-01","48"
"2012-02","10"
"2012-03","218469"
"2012-04","187936"
"2012-05","122416"
"2012-06","170591"
"2012-07","204978"
"2012-08","144725"
"2012-09","203517"
"2012-10","113035"
"2012-11","50841"
"2012-12","5205"
"2013-01","17040"
"2013-02","167338"
"2013-03","123992"
"2013-04","32927"
"2013-05","272112"
"2013-06","301422"
"2013-07","267637"
"2013-08","291223"
"2013-09","187944"
"2013-10","273702"
"2013-11","129161"
"2013-12","52017"
"2014-01","119008"
"2014-02","207972"
"2014-03","69020"
"2014-04","11295"
"2014-05","38454"
"2014-06","311463"
"2014-07","99155"
"2014-08","81376"
"2014-09","38114"

SELECT  substr( datetime(closed_at, 'unixepoch'),0,8), sum(num_changes)   FROM osm_changeset WHERE osm_user='ediyes'   group by substr( datetime(closed_at, 'unixepoch'),0,8)  order by substr( datetime(closed_at, 'unixepoch'),0,8)  


"2013-02","295"
"2013-04","53"
"2013-11","201748"
"2013-12","160245"
"2014-01","196844"
"2014-02","153093"
"2014-03","181156"
"2014-04","194561"
"2014-05","106173"
"2014-06","213692"
"2014-07","150458"
"2014-08","111666"
"2014-09","51779"




SELECT  substr( datetime(closed_at, 'unixepoch'),0,8), sum(num_changes)   FROM osm_changeset WHERE osm_user='Luis36995'   group by substr( datetime(closed_at, 'unixepoch'),0,8)  order by substr( datetime(closed_at, 'unixepoch'),0,8)  



"2013-12","13293"
"2014-01","64694"
"2014-02","88394"
"2014-03","148310"
"2014-04","192982"
"2014-05","228157"
"2014-06","188663"
"2014-07","89733"
"2014-08","79601"
"2014-09","6484"

SELECT  substr( datetime(closed_at, 'unixepoch'),0,8), sum(num_changes)   FROM osm_changeset WHERE osm_user='dannykath'   group by substr( datetime(closed_at, 'unixepoch'),0,8)  order by substr( datetime(closed_at, 'unixepoch'),0,8)  

"2014-08","20920"
"2014-09","25259"


SELECT  substr( datetime(closed_at, 'unixepoch'),0,8), sum(num_changes)   FROM osm_changeset WHERE osm_user='RichRico'   group by substr( datetime(closed_at, 'unixepoch'),0,8)  order by substr( datetime(closed_at, 'unixepoch'),0,8)  


"2014-08","25925"
"2014-09","37259"

### Numero de cnabios por Mes
SELECT  substr( datetime(closed_at, 'unixepoch'),0,8), count(*)   FROM osm_changeset WHERE osm_user='Rub21'  group by substr( datetime(closed_at, 'unixepoch'),0,8)  order by substr( datetime(closed_at, 'unixepoch'),0,8)  

"2011-08","69"
"2011-09","189"
"2011-10","36"
"2012-01","8"
"2012-02","3"
"2012-03","423"
"2012-04","110"
"2012-05","66"
"2012-06","280"
"2012-07","532"
"2012-08","452"
"2012-09","754"
"2012-10","1016"
"2012-11","580"
"2012-12","17"
"2013-01","70"
"2013-02","580"
"2013-03","799"
"2013-04","148"
"2013-05","1091"
"2013-06","1594"
"2013-07","1679"
"2013-08","1349"
"2013-09","1011"
"2013-10","1549"
"2013-11","547"
"2013-12","384"
"2014-01","701"
"2014-02","682"
"2014-03","568"
"2014-04","42"
"2014-05","78"
"2014-06","694"
"2014-07","3108"
"2014-08","636"
"2014-09","288"

SELECT  substr( datetime(closed_at, 'unixepoch'),0,8), count(*)   FROM osm_changeset WHERE osm_user='ediyes'  group by substr( datetime(closed_at, 'unixepoch'),0,8)  order by substr( datetime(closed_at, 'unixepoch'),0,8)  
"2013-02","4"
"2013-04","3"
"2013-11","1306"
"2013-12","855"
"2014-01","1106"
"2014-02","474"
"2014-03","848"
"2014-04","975"
"2014-05","1455"
"2014-06","879"
"2014-07","3589"
"2014-08","3626"
"2014-09","1894"

SELECT  substr( datetime(closed_at, 'unixepoch'),0,8), count(*)   FROM osm_changeset WHERE osm_user='Luis36995'  group by substr( datetime(closed_at, 'unixepoch'),0,8)  order by substr( datetime(closed_at, 'unixepoch'),0,8)  


"2013-12","782"
"2014-01","1995"
"2014-02","282"
"2014-03","465"
"2014-04","582"
"2014-05","520"
"2014-06","371"
"2014-07","4091"
"2014-08","2150"
"2014-09","216"

SELECT  substr( datetime(closed_at, 'unixepoch'),0,8), count(*)   FROM osm_changeset WHERE osm_user='dannykath'  group by substr( datetime(closed_at, 'unixepoch'),0,8)  order by substr( datetime(closed_at, 'unixepoch'),0,8)  

"2014-08","1826"
"2014-09","1754"

SELECT  substr( datetime(closed_at, 'unixepoch'),0,8), count(*)   FROM osm_changeset WHERE osm_user='RichRico'  group by substr( datetime(closed_at, 'unixepoch'),0,8)  order by substr( datetime(closed_at, 'unixepoch'),0,8)  


"2014-08","1880"
"2014-09","3217"

SELECT  substr( datetime(closed_at, 'unixepoch'),0,11), sum(num_changes)   FROM osm_changeset WHERE osm_user='Rub21'  and  closed_at > 1408060800  group by substr( datetime(closed_at, 'unixepoch'),0,11)  order by substr( datetime(closed_at, 'unixepoch'),0,11) 




SELECT substr( datetime(closed_at, 'unixepoch'),0,8) ,  count(num_changes)  FROM osm_changeset   group by substr( datetime(closed_at, 'unixepoch'),0,8)  order by substr( datetime(closed_at, 'unixepoch'),0,8)  