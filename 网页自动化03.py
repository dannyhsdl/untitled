#from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver=webdriver.Chrome('F:\chrome.exe')
# driver.get('https://www.timeanddate.com')
#
# selectelements=driver.find_element_by_id('month')
# months=Select(selectelements)
# months.select_by_visible_text('December')
#
# countryelements=driver.find_element_by_id('country')
# countries=Select(countryelements)
# countries.select_by_visile_text('Taiwan')
#
# driver.find_element_by_xpath("//input[@value='View Calendar']").click()
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome("F:\chromedriver.exe")
driver.fullscreen_window()
driver.get("https://www.timeanddate.com")

selectelements=driver.find_element_by_id('month')
months=Select(selectelements)
months.select_by_visible_text('February')

countrieselements=driver.find_element_by_id('country')
countries=Select(countrieselements)
countries.select_by_visible_text('China')

driver.find_element_by_xpath("//form[@id='cf']//input[@value='View Calendar']").click()

time.sleep(10)
driver.quit()
# selenium go to pypi(by google search engine)
# install selenium first then use this momodel
# hope you like this



