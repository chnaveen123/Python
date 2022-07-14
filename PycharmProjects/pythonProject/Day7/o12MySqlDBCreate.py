
"""
1. pymysql
2. mysqldb
3. mysql.connector
"""
import pymysql

# Query String
conn = pymysql.connect(host="localhost", user="root", password="Temp1234", port=3306)

cursor = conn.cursor()

query = "create database players"

cursor.execute(query)

conn.close()