#调用浏览器
# 导入库
import time
from selenium import webdriver
dri=webdriver.Chrome('D:\pccj\chromedriver.exe')
#dri.fullscreen_window()
#访问这个网站
dri.get('https://wallhaven.cc')
# dri.get('https://baidu.com')
# dri.get('https://YouTube.com')
# dri.get('https://google.com')
#最大化
dri.maximize_window()
#找到这个ID点击
# dri.find_element_by_id("search-text").click()
# #找到这个输入框输入 .
# dri.find_element_by_id("search-text").send_keys('sky')
#通过name找到输入并框输入
#dri.find_element_by_name('q').send_keys('sky\n')
#休眠2秒钟
#time.sleep(5)
#关闭网页
#dri.quit()
#通过链接名字点击
# dri.find_element_by_link_text('anime').click()
#返回
#dri.back()
#部分链接
#dri.find_element_by_partial_link_text('nime').click()
#通过tag名字找到网页中想要的并点击
# elments=dri.find_elements_by_tag_name('a')
# for elment in elments:
#     if 'Toplist' in elment.text:
#         elment.click()
#dri.find_element_by_id('search-submit').click()
#通过xpath找元素
#dri.find_element_by_xpath("//a[contains(text(),'Login')]").click()
#通过css查找
#dri.find_element_by_css_selector("#search-text").send_keys('sky\n')
dri.save_screenshot("D:\jie.png")
