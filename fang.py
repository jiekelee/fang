#coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://zjj.jiangmen.gov.cn/index_rsfjytj.html")
# assert u"百度" in driver.title
time.sleep(5)
print driver.page_source
driver.close()