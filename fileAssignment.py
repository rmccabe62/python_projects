
#import sqlite3 to work with a database
import sqlite3
# connect to database using sqlite3
conn = sqlite3.connect('test.db')
# create a table with fields
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name TEXT)")
    conn.commit()

conn.close()

conn = sqlite3.connect('test.db')
# create a variable list to pull from
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
# for loop including if conditional statement to query text files from list
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # insert values into table to query
            cur.execute("INSERT INTO tbl_fileList(col_name) VALUES (?)",(x,))
            cur.execute("INSERT INTO tbl_fileList(col_name) VALUES (?)",(x,))
        print(x)
    conn.commit()
conn.close()



   
