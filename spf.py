import time
from selenium import webdriver
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import sqlite3
import datetime

display=Display(visible=0,size=(800,800))
display.start()
driver=webdriver.Chrome()
driver.get('http://zjj.jiangmen.gov.cn/index_spfjytj.html')
time.sleep(5)
# title=driver.title
# print(title.encode('utf-8'))
# print driver.page_source
html = driver.page_source
driver.close()
display.stop()

soup = BeautifulSoup(html,'html.parser')
results = soup.find_all('td')[-42:]

conn = sqlite3.connect('fang.db')
c = conn.cursor()

for area in ['pengcheng','beixin','chaohe','duyuan','bintang','jianghai']:
    # print area    
    results.pop(0)
    line = results[0:6]
    # print '------------------'
    datas = []

    for result in line:
        num = result.get_text().strip()
        if num is None or num == '':
            num = 0
        datas.append(num)
        results.pop(0)

    # print datas[0]
    sum_acreage = float(datas[0])
    sum_amount = float(datas[1])
    sum_num = int(datas[2])
    z_acreage = float(datas[3])
    z_amount = float(datas[4])
    z_num = int(datas[5])
    isnew = 'new'    

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = 'insert into Spf(gettime,area,sum_acreage,sum_amount,sum_num,z_acreage,z_amount,z_num,isnew)'
    c.execute(sql + 'values("{0}","{1}",{2},{3},{4},{5},{6},{7},"{8}")'.format(now,area,sum_acreage,sum_amount,sum_num,z_acreage,z_amount,z_num,isnew))

result = c.execute('select * from Spf')
for r in result:
    print r
conn.commit()
conn.close()



        

