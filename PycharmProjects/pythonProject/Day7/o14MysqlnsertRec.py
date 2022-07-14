
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="Temp1234", database="players", port=3306)

cur = conn.cursor()

#query = "insert into player values ('PLY101', 'Sachin Tendulkar', 'Cricket', 'India', '38750 runs')"
#query = "insert into player values ('PLY235', 'Cristiano Ronaldo', 'soccer', 'Portugese', '450 goals')"
#query = "insert into player values ('PLY310', 'Mike Tyson', 'Boxing', 'USA', '85 knock outs')"
query = "insert into player values ('PLY498', 'Roger Fedrer', 'Tennis', 'Switzerland', '65 grand slams')"
#query = "insert into player values ('PLY525', 'PV Sindhu', 'Badminton', 'India', '5 major medals')"
cur.execute(query)

conn.commit()

conn.close()