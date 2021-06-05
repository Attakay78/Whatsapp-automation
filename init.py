from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input("Enter name of user")
msg = input("Enter your message")
count = input("Enter the count")