import sqlite3

conn=sqlite3.connect("db.db")
c=conn.cursor()
createTable = "CREATE TABLE land_info(land varchar(32), price int, address varchar(32), area int)"
