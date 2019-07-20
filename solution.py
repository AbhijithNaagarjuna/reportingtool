import psycopg2
import numpy as np
import re
from datetime import datetime


print("The most errors occured on : ")
db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute("select day from (select date(time) as day, count(id) as errors from log where status != '200 OK' group by day order by errors desc limit 1) as seq")
t = c.fetchall()
res = datetime.strftime(t[0][0],'%b %d, %Y')
print(res)
db.close()

print("")
print("The most viewed articles are :")

db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute(" select articles.title,logd.views from articles,logd where articles.slug = logd.substring order by views desc limit 5")
res = c.fetchall()
out = np.asarray(res)
for x in range(len(out)): 
  print str(out[x])[1:-2] + " Views'"
db.close()

print("")
print("The most popular Authors are")

db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute("select authors.name,sum(authord.views) from authors,authord where authord.author = authors.id group by name order by sum desc")
res = c.fetchall()
outt = np.asarray(res)
for x in range(len(outt)): 
  print str(outt[x])[1:-1] + "Views"
db.close()