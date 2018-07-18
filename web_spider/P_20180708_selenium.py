from selenium import webdriver

browser=webdriver.Chrome()
print(type(browser))
browser.get('http://www.huaban.com')
m=browser.find_element_by_tag_name('img')
print(m)