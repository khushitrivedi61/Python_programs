import mysql.connector

mydb = mysql.connector.connect (
    host= "localhost",
    user="root",
    password="",
    database="college"
)
a=mydb.cursor()

a.execute("create table customers(name varchar(225), address varchar(225))")

if a:
a.execute("table created")
