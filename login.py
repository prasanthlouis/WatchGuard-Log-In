from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import urllib2

y=0

x='https://10.0.3.12:4100/?action=fw_logon&style=fw_logon_success.xsl&fw_logon_type=status&action=fw_logon&style=fw_logon.xsl&fw_logon_type=status&redirect=http://10.0.3.12/'

driver = webdriver.Firefox()

for y in range(1,1000):	
	driver.get("https://10.0.3.12:4100/wgcgi.cgi?action=fw_logon&style=fw_logon.xsl&fw_logon_type=status&redirect=http://10.0.3.12/")
	time.sleep(2)
	print driver.current_url

	if driver.current_url==x:
		continue


	username = driver.find_element_by_name("fw_username")
	password = driver.find_element_by_name("fw_password")
	
	username.send_keys("")
	username.send_keys(Keys.CONTROL + "a");
	username.send_keys(Keys.DELETE);
	username.send_keys("Enter user name here")
	
	password.send_keys("Enter password here")

	driver.find_element_by_name("submit").click()

	
