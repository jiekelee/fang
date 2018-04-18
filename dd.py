from selenium import webdriver
from pyvirtualdisplay import Display
# Add following 2 line before start the Chrome
display = Display(visible=0, size=(800, 800))  
display.start()
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.quit()
display.stop()