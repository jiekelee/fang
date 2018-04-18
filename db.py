import sqlite3
import datetime

conn = sqlite3.connect('fang.db')
c = conn.cursor()

# c.execute('create table bc(id integer primary key,name varchar(20),get_t datetime,num float)')
# c.execute('''CREATE TABLE Spf(tid integer PRIMARY KEY,
#     gettime datetime,
#     area char(6),
#     sum_acreage float,
#     sum_amount float,
#     sum_num integer,
#     z_acreage float,
#     z_amount float,
#     z_num integer)''')
# c.execute('insert into test(id,name)values(1,"jack")')
# c.execute('insert into bc(name,get_t,num)values("hugo","{}",20.2)'.format(datetime.datetime.now()))
# c.execute('insert into Spf(gettime,area,sum_acreage,sum_amount,sum_num,z_acreage,z_amount,z_num)values("{}","all",23.32,900,40,49.52,800,23)'.format(datetime.datetime.now()))
result = c.execute('delete from Spf')
for r in result:
	print r
conn.commit()
conn.close()