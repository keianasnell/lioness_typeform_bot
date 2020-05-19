#!/usr/bin/env python
from selenium import webdriver
from joblib import Parallel, delayed
import time

def send_lioness_form(url):
	count = 0

	chromedriver_location = "/Users/keianarei/Desktop/chromedriver"
	driver = webdriver.Chrome(chromedriver_location)
	driver.get(url)

	while count < 5:
		#first_name = '//*[@id="shortText-b68e67ad-e3c8-47a1-8c32-e3fca817d623-QVWINiVA3l08Q6DE"]'
		first_name = driver.find_element_by_xpath('//*[contains(@id, "shortText-b68e67ad-e3c8-47a1-8c32-e3fca817d623")]')
		
		driver.implicitly_wait(10)
		time.sleep(1)
		first_name.send_keys('Keiana')


		driver.implicitly_wait(10)
		search = driver.find_element_by_xpath("//*[@type='text']")
		search.send_keys(u'\ue007')
		# okay_btn = driver.find_element_by_xpath('//*[@id="block-b68e67ad-e3c8-47a1-8c32-e3fca817d623"]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')
		# driver.implicitly_wait(10)
		# okay_btn.click()

		email_address = driver.find_element_by_xpath('//*[contains(@id, "email-23fbded0-0dc9-4b47-b5c5-d97d1446ca3f")]')
		email_address.send_keys('keianarei@gmail.com')

		# search = driver.find_element_by_xpath("//*[@type='text']")
		# search.send_keys(u'\ue007')
		okay_btn_2 = driver.find_element_by_xpath('//*[@id="block-23fbded0-0dc9-4b47-b5c5-d97d1446ca3f"]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')
		okay_btn_2.click()

		time.sleep(1)
		day = driver.find_element_by_xpath('//*[contains(@data-qa, "date-input-day")]')
		day.send_keys('28') 
		month = driver.find_element_by_xpath('//*[contains(@data-qa, "date-input-month")]')
		month.click()
		driver.implicitly_wait(10)
		month.send_keys('7')
		year = driver.find_element_by_xpath('//*[contains(@data-qa, "date-input-year")]')
		year.click()
		year.send_keys('1998')	


		submit_btn = driver.find_element_by_xpath('//*[@id="block-528fc958-9e33-4ef1-ac36-65fe80d58de2"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div/div/button')
		submit_btn.click()
		# print("Submitted!")
		count = count + 1

		time.sleep(2)

		driver.refresh()


urls = ['https://lionessfashion932692.typeform.com/to/Ki2k2l', 'https://lionessfashion932692.typeform.com/to/Ki2k2l', 'https://lionessfashion932692.typeform.com/to/Ki2k2l','https://lionessfashion932692.typeform.com/to/Ki2k2l']

Parallel(n_jobs=-1)(delayed(send_lioness_form)(url) for url in urls)

