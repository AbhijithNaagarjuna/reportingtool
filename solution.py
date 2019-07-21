# ! /usr/bin/python
# THE FOLLOWING VIEW TABLES HAVE BEEN USED
# LOGD - VIEW TABLE
# AUTHORD - VIEW TABLE


import psycopg2
import numpy as np
import re
from datetime import datetime

# CODE TO FIND OUT THE MOST ERRORS OCCURED ON A PARTICULAR DAY
print(The most errors occured on)
db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute("""select day from
(select date(time) as day, count(id) as errors from log
where status != '200 OK'
group by day order by errors desc limit 1) as seq""")
t = c.fetchall()
res = datetime.strftime(t[0][0], '%b %d, %Y')
print(res)
db.close()
print()
print(The most viewed articles are)

# CODE TO FIND OUT THE MOST VIEWED ARTICLES
db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute(""" select articles.title,logd.views from articles,logd
where articles.slug = logd.substring order by views desc limit 5""")
res = c.fetchall()
for x in range(len(res)):
    print(str(res[x][0])+"--"+str(res[x][1]) + " Views")
db.close()

print()
print(The most popular Authors are)

# CODE TO FIND OUT THE MOST POPULAR AUTHORS
db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute("""
select authors.name,sum(authord.views) from authors,authord
where authord.author = authors.id group by name order by sum desc""")
res = c.fetchall()
for x in range(len(res)):
    print(str(res[x][0])+"--"+str(res[x][1]) + " Views")
db.close()
