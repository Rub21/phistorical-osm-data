SELECT SUM(num_changes) FROM osm_changeset WHERE osm_user='Rub21'

4,538,100



SELECT SUM(num_changes) FROM osm_changeset WHERE osm_user='ediyes'

1,721,763

SELECT SUM(num_changes) FROM osm_changeset WHERE osm_user='Luis36995'

1,100,311

SELECT SUM(num_changes) FROM osm_changeset WHERE osm_user='dannykath'

46,179

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



SELECT  sum(num_changes) ,substr( datetime(closed_at, 'unixepoch'),0,8)  FROM osm_changeset WHERE osm_user='Luis36995'   group by substr( datetime(closed_at, 'unixepoch'),0,8)  order by substr( datetime(closed_at, 'unixepoch'),0,8)  
"13293","2013-12"
"64694","2014-01"
"88394","2014-02"
"148310","2014-03"
"192982","2014-04"
"228157","2014-05"
"188663","2014-06"
"89733","2014-07"
"79601","2014-08"
"6484","2014-09"

SELECT  sum(num_changes) ,substr( datetime(closed_at, 'unixepoch'),0,8)  FROM osm_changeset WHERE osm_user='dannykath'   group by substr( datetime(closed_at, 'unixepoch'),0,8)  order by substr( datetime(closed_at, 'unixepoch'),0,8)  


"20920","2014-08"
"25259","2014-09"




