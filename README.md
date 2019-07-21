# reportingtool
Basic Reporting tool for Queries

STEPS TO RUN IT :
Step 1 : Bring the virtual machine online (with vagrant up). Then log into it with vagrant ssh.
Step 2 : cd into the vagrant
Step 3 : Connect to the new database by running the following command
Step 4 : Execute the below view tables
Step 5 : Execute the python solution.py




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
