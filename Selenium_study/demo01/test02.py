from selenium import webdriver


wd = webdriver.Chrome()
wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
list = wd.find_elements_by_class_name('animal')
print(list)
# ele = wd.find_element_by_id('searchtext')
# ele.send_keys('hui le ma ')

pass




