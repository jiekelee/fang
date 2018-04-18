import time
from selenium import webdriver
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import sqlite3
import datetime

display=Display(visible=0,size=(800,800))
display.start()
driver=webdriver.Chrome()
driver.get('http://zjj.jiangmen.gov.cn/index_rsfjytj.html')
time.sleep(5)
# title=driver.title
# print(title.encode('utf-8'))
# print driver.page_source
html = driver.page_source
driver.close()
display.stop()

soup = BeautifulSoup(html,'html.parser')
result = soup.find_all('td')[-6:]
data = []
for r in result:
    # print r.get_text().strip()
    data.append(r.get_text().strip()) 
# print data[1]
area = 'all'
sum_acreage = data[0]
sum_amount = data[1]
sum_num = data[2]
z_acreage = data[3]
z_amount = data[4]
z_num = data[5]
isnew = 'old'

# print sum_num
conn = sqlite3.connect('fang.db')
c = conn.cursor()

# sql = 'drop table Spf'
# c.execute(sql)

# c.execute('''CREATE TABLE Spf(tid integer PRIMARY KEY,
#     gettime datetime,
#     area char(6),
#     sum_acreage float,
#     sum_amount float,
#     sum_num integer,
#     z_acreage float,
#     z_amount float,
#     z_num integer,
#     isnew char(3))''')

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
sql = 'insert into Spf(gettime,area,sum_acreage,sum_amount,sum_num,z_acreage,z_amount,z_num,isnew)'
c.execute(sql + 'values("{0}","{1}",{2},{3},{4},{5},{6},{7},"{8}")'.format(now,area,sum_acreage,sum_amount,sum_num,z_acreage,z_amount,z_num,isnew))


result = c.execute('select * from Spf')
for r in result:
    print r
conn.commit()
conn.close()