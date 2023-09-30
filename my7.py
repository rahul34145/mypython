import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='admin')
cur=mydb.cursor()
cur.execute("create database db1")