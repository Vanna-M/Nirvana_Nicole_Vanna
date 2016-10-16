import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops


#make table the first
q = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
c.execute(q)    #run SQL query

#open csv
fObj = open("peeps.csv")
#read csv
d=csv.DictReader(fObj)
#add csv into table
for k in d:
    p = "INSERT INTO students VALUES (\'" + k['name'] + "\'," + k['age'] + "," + k['id'] + ")"
    c.execute(p)

#make table the second
q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
c.execute(q)

#open csv the second
fObj = open("courses.csv")
#read csv
d = csv.DictReader(fObj)

#add csv into table
for k in d:
    p = "INSERT INTO courses VALUES(\'"+k['code'] + "\'," + k['id'] + "," + k['mark']+")"
    c.execute(p)

db.commit() #save changes

db.close()  #close database
