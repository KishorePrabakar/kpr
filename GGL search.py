from selenium import webdriver
x = input("Search topic: ")
x = x.replace(' ', '+')
browser = webdriver.Chrome('chromedriver')
for i in range(1):
    browser.get("https://www.google.com/search?q=" + x + "&start" + str(i))

