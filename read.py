from bs4 import BeautifulSoup
import requests
import re
import time
import pandas as pd

url=r''#place link between quotes
a=re.search(r'.*.com/',url)
main_url=a[0]
print("Main url: ",main_url)

# extraccion de URL de celulares
a=requests.get(url)
b=BeautifulSoup(a.content,'html.parser')

checkphones={}
# lista de links de celulares
for c in b.find_all('a'):
    d=c.get('href')
    e=re.search(r'(.*)-[0-9]*.php$',d)
    if e!=None and re.search(r'phones',e[0])==None:
        phone_name=re.sub(r'[-_]',' ',e[1])
        checkphones[phone_name]=main_url+e[0]

print("Checkphones dictionary",checkphones.keys())

#generacion de archivo de celular y su respectivo link
with open('celulares compra.txt','w') as f:
    for a in checkphones.keys():
        print(a.strip())
        print(checkphones[a])
        print("")
        f.write("{}: {}\n".format(a.strip(),checkphones[a]))
