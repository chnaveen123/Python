
import pymysql
from prettytable import from_db_cursor

conn = pymysql.connect(host="localhost", user="root", password="Temp1234", database="players", port=3306)

cur = conn.cursor()

query = "select * from player"

cur.execute(query)

pt = from_db_cursor(cur)
pt.align['plyName'] = "l"
pt.align['sport'] = "l"
pt.align['country'] = "l"
pt.align['acheivement'] = "l"

# for row in cur.fetchall():
#     print(row)

conn.close()

print(pt)