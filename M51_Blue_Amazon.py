import requests
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from lib2to3.fixer_util import String
from msilib import text

# driver = webdriver.Chrome("ChromeDriver")
driver = webdriver.Chrome()

products=[]
source=[] 
price=[] 
category=[] 
modelno=[]
driver.get("https://www.amazon.in/Samsung-Galaxy-Electric-Blue-128GB-Storage/dp/B085J1868F/ref=sr_1_1_sspa?dchild=1&keywords=mobile&qid=1611926665&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFRQjFCTjBXVVcwMjEmZW5jcnlwdGVkSWQ9QTAzODEyMTcxOTVQNTlSVlVNVzE2JmVuY3J5cHRlZEFkSWQ9QTAwMTg3NzBGVzRUUTFHOVJaSEkmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl")

content =driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':''}):
	name=a.find('div' ,attrs={'class':'a-size-large product-title-word-break'})
	source=a.find('div' ,attrs={'class':'nav-logo-link nav-progressive-attribute'})
	price=a.find('div' , attrs={'class':'a-size-medium a-color-price priceBlockBuyingPriceString'})
	category=a.find('div' , attrs={'class':'a-size-base prodDetAttrValue'})
	modelno=a.find('div' , attrs={'class':'a-size-base prodDetAttrValue'})

products.append(String(name))
source.append(String(source))
price.append(String(price))
category.append(String(category))
modelno.append(String(modelno))

df = pd.DataFrame({'Product Name':products,'Source':source,'Price':price,'Category':category,'Model No':modelno})
df.to_csv('products.csv', index=False, encoding='utf-8')