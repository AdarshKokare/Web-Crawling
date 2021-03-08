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
driver.get("https://www.flipkart.com/poco-m2-slate-blue-64-gb/p/itmfd82e37cf60fb?pid=MOBFV9V96DHYMUHJ&lid=LSTMOBFV9V96DHYMUHJLEC0DY&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&fm=SEARCH&iid=28b15cef-6f29-400e-838c-28493b44b89f.MOBFV9V96DHYMUHJ.SEARCH&ppt=sp&ppn=sp&ssid=qs5b3rtje80000001611927010940&qH=eb4af0bf07c16429")

content =driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':''}):
	name=a.find('div' ,attrs={'class':'B_NuCI'})
	source=a.find('div' ,attrs={'class':'_2xm1JU'})
	price=a.find('div' , attrs={'class':'_30jeq3 	_16Jk6d'})
	category=a.find('div' , attrs={'class':'_21lJbe'})
	modelno=a.find('div' , attrs={'class':'_21lJbe'})

products.append(String(name))
source.append(String(source))
price.append(String(price))
category.append(String(category))
modelno.append(String(modelno))

df = pd.DataFrame({'Product Name':products,'Source':source,'Price':price,'Category':category,'Model No':modelno})
df.to_csv('products.csv', index=False, encoding='utf-8')