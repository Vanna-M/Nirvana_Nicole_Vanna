import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#get wanted info
q = "SELECT name, students.id, courses.id, mark FROM students, courses WHERE students.id=courses.id"

sel = c.execute(q)    #run SQL query

d={} # {name:[id,sumOfScores,numOfScores]}

for m in sel:
    name=m[0]
    id=m[1]
    num=m[3]   
    if (name not in d.keys()):
        d[name]=[0,0,0] # create a dict slot
        d[name][0] = id # set its id
    d[name][1] += num # add to sum
    d[name][2] += 1 # add to num of scores

    
print "[name,id,avg]"

for n in d:
    print "["+n+","+str(d[n][0])+","+str(float(d[n][1])/d[n][2])+"]"

