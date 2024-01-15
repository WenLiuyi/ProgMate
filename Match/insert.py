import sqlite3
import pandas as pd

def getTuple(name,cur):
    sql1 = "SELECT * FROM OBJECTS WHERE NAME='%s'"%name
    if('\''in name or '\"' in name): return False
    print(name)
    cur.execute(sql1)
    list=cur.fetchone()
    if list is not None:
        #list = cur.fetchone()
        sql2 = "UPDATE OBJECTS SET FREQ='%d' WHERE NAME='%s'" % (list[1] + 1, name)
        cur.execute(sql2)
        return True
    else:
        sql2 = "INSERT INTO OBJECTS VALUES('%s','%d')" % (name,1)
        cur.execute(sql2)
        return False

def insertTable(cws,pos,cur):
    print("hello")
    num=len(cws)
    i=0

    while(i<num):
        if(i+3<num):
            if(pos[i]=='n' and pos[i+1]=='v' and pos[i+2]=='v' and pos[i+3]=='v'):
                name=cws[i]+cws[i+1]+cws[i+2]+cws[i+3]
                getTuple(name,cur);i+=4;continue

        if (i+2<num):
            if(pos[i]=='d' and pos[i+1]=='a' and pos[i+2]=='n'):
                name = cws[i] + cws[i + 1] + cws[i + 2]
                getTuple(name,cur);i += 3;continue

            elif (pos[i] == 'b' and pos[i + 1] == 'q' and pos[i + 2] == 'v'):
                name = cws[i] + cws[i + 1] + cws[i + 2]
                getTuple(name,cur);i += 3;continue

            elif (pos[i] == 'ws' and pos[i + 1] == 'wp' and pos[i + 2] == 'n'):
                name = cws[i] + cws[i + 1] + cws[i + 2]
                getTuple(name,cur);i += 3;continue

        if (i + 1 < num):
            if (pos[i] == 'v' and pos[i + 1] == 'n'):
                name = cws[i] + cws[i + 1]
                getTuple(name,cur);
                i += 2;
                continue

            elif (pos[i] == 'n' and pos[i + 1] == 'n'):
                name = cws[i] + cws[i + 1]
                getTuple(name,cur);
                i += 2;
                continue

            elif (pos[i] == 'n' and pos[i + 1] == 'v'):
                name = cws[i] + cws[i + 1]
                getTuple(name,cur);
                i += 2;
                continue

            elif (pos[i] == 'ws' and pos[i + 1] == 'n'):
                name = cws[i] + cws[i + 1]
                getTuple(name,cur);
                i += 2;
                continue

            elif (pos[i] == 'm' and pos[i + 1] == 'n'):
                name = cws[i] + cws[i + 1]
                getTuple(name,cur);
                i += 2;
                continue

            elif (pos[i] == 'nd' and pos[i + 1] == 'v'):
                name = cws[i] + cws[i + 1]
                getTuple(name,cur);
                i += 2;
                continue

        if(pos[i]=='n'):
            getTuple(cws[i],cur);

        elif (pos[i] == 'ws'):
            getTuple(cws[i],cur);

        i+=1
        continue