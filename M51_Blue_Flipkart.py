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
driver.get("https://www.flipkart.com/samsung-galaxy-m51-electric-blue-128-gb/p/itm4c319bae3c362?pid=MOBFX2HBBH8BSPTE&lid=LSTMOBFX2HBBH8BSPTEZVPIZM&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=33a99187-5a78-4ef6-8559-bf9afc3ce4cb.MOBFX2HBBH8BSPTE.SEARCH&ppt=sp&ppn=sp&ssid=30b8m1p1b40000001611926940585&qH=e6993039c9103e97")

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

