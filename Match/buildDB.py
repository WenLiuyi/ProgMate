import sqlite3,match
from sqlite3 import OperationalError

con=sqlite3.connect("../Objects.db")
cur=con.cursor()
print("connect success")

con.execute('''CREATE TABLE OBJECTS
       (NAME           TEXT    NOT NULL,
       FREQ            INT     NOT NULL
       );''')
#con.execute("DROP TABLE OBJECTS")

text_dir="../DataFormat/text"
match.read_text_all(text_dir,cur)

con.close()
