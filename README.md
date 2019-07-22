## reportingtool
Basic Reporting tool for Queries

PYTHON VERSION 2.7

DEPENDENCIES : 
psycopg2
numpy
re
from datetime import datetime



STEPS TO RUN IT :
Step 1 : Bring the virtual machine online (with vagrant up). Then log into it with vagrant ssh.
Step 2 : cd into the vagrant
Step 3 : Dowload the newsdata.sql file from the following link https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
Step 4 : Extract it to the same folder as Vagrant
Step 4 : Connect to the new database by running the following command psql -d news -f newsdata.sql
Step 5 : Execute the below view tables
Step 6 : Execute the python solution.py




VIEW TABLES : 

CREATE VIEW logd AS SELECT "substring"(log.path, 10) AS "substring",
    count(log.path) AS views
   FROM log
  WHERE log.status = '200 OK'::text AND log.path ~~ '/%%'::text
  GROUP BY log.path
  ORDER BY (count(log.path))
 LIMIT 8;

CREATE VIEW authord AS  SELECT articles.author,
    articles.title,
    logd.views
   FROM articles,
    logd
  WHERE articles.slug = logd."substring"
  ORDER BY logd.views DESC;
