import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


#connect to proper db
f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops


q = "SELECT * FROM students"
c.execute(q)
#all entries in students
students = c.fetchall()

#print each student on new line (prettier)
for i in students:
    print i

print "--------------------"

q = "SELECT * FROM courses"
c.execute(q)
#all entries in courses
courses = c.fetchall()

#print each course on new line
for i in courses:
    print i

db.close() #close database
