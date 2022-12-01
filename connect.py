import mysql.connector as mq

from mysql.connector import errorcode
from tabulate import tabulate


conn = mq.connect(host = 'localhost',user ='root', password = 'YU_oppdivide!20',db = 'menagerie')
print("Connected")

connections = conn.cursor()



def showdb():

    print("MySQL Databases")

    showdb = "show databases"

    connections.execute(showdb) 

    for showdb in connections:

        print (f"{showdb[0]}")
showdb()


'''def dropmg():

    c.execute('DROP DATABASE IF EXISTS menagerie')
    c.execute('CREATE DATABASE menagerie')

    print('Database has been dropped')

dropmg()'''



def pettableshow():

    connections.execute("DESCRIBE pet")
    print(connections.fetchall())

pettableshow()

def tape():
    connections.execute("INSERT INTO pet (name,owner,species,sex,birth,death) VALUES \
    ('Fluffy','Harold', 'cat', 'f','1993-02-04',NULL),\
    ('Claws','Gwen', 'cat', 'm','1994-03-17',NULL),\
    ('Buffy','Harold', 'dog', 'f','1989-05-13',NULL),\
    ('Fang','Benny', 'dog', 'm','1990-08-27',NULL),\
    ('Bowser','Diane', 'dog', 'm','1979-08-31','1995-07-29'),\
    ('Chripy','Gwen', 'bird', 'f','1998-09-11',NULL),\
    ('Whistler','Gwen', 'bird', 'NULL','1997-12-09',NULL),\
    ('Slim','Benny', 'snake', 'm','1996-04-29',NULL),\
    ('Puffball','Diane', 'hamster', 'f','1999-03-30',NULL)")

conn.commit()

print("Data has been loaded.")
tape()

def pettabledata():

#display pettable data

    connections.execute('SELECT * FROM pet')

    pd = connections.fetchall()



    for i in pd:

        print(i[0], i[1], i[2], i[3], i[4], i[5])

pettabledata()



def femdogs():

#display female dogs

    connections.execute("SELECT * FROM pet WHERE sex = 'f' AND species = 'dog';")

    pd = connections.fetchall()



    for i in pd:

        print(i[0], i[1], i[2], i[3], i[4], i[5])

femdogs()



def namebirth():

#displayname birth

    connections.execute("SELECT * FROM pet;")

    pd = connections.fetchall()



    for i in pd:

        print(i[0], i[4])

namebirth()



def owners():

#display owners

    connections.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner;")

    pd = connections.fetchall()



    for i in pd:

        print(i[0], i[1])

owners()



def months():

#display months

    connections.execute("SELECT name, birth, MONTH(birth) FROM pet;")

    pd = connections.fetchall()



    print(tabulate(pd, headers= ['name','birth','MONTH(birth)'], tablefmt='psql'))

months()