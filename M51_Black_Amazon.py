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
driver.get("https://www.amazon.in/Samsung-Galaxy-Celestial-Black-Storage/dp/B085J1CPCW/ref=sr_1_1?dchild=1&keywords=SM-M515FZKEINS&qid=1611926964&sr=8-1")

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