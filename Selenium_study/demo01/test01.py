from selenium import webdriver
import time
wd = webdriver.Chrome()
wd.implicitly_wait(15)      # 设置该时间后，一旦元素没有找到时，并不立即报异常，而是每隔半秒种再去寻找，持续10秒
wd.get('https://www.baidu.com')
ele = wd.find_element_by_id('kw')
ele.send_keys('白月黑羽')
print(ele.get_attribute('value'))    # 'value'获取输入框内的输入文本
ele = wd.find_element_by_id('su')
ele.click()

# time.sleep(1)

ele = wd.find_element_by_id('1')
print(ele.text)

print(ele.get_attribute('srcid'))
# print(ele.get_attribute('outerHTML'))    # 通过'outerHTML'获取该元素的整个html
print(ele.get_attribute('innerHTML'))    # 通过'innerHTML'获取该元素的内部的html

ele = wd.find_element_by_css_selector('#searchtext')    # 根据class去寻找用'.'  , 根据id寻找用 '#'

wd.quit()

