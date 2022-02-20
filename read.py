from bs4 import BeautifulSoup
import requests
import re
import time
import pandas as pd

url=r'https://www.gsmarena.com/results.php3?nYearMin=2018&nRamMin=3000&nRamMax=12000&nIntMemMin=32000&fDisplayInchesMax=5.5&chkUSBC=selected&sAvailabilities=1&sOSes=2'
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

# feature extraction de celulares
# interesa: size (diagonal), announced date, status=available, 
# Interal memory (RAM y ROM), NFC=YES, USB=usb C, IP rating= 67/68
# battery size (mah), bandas compatibles, # de SIM

# features={}
# for e,a in checkphones.items():
#     print("Checking info for:",e)
#     features[e]={}
#     b=requests.get(a)
#     c=BeautifulSoup(b.content,'html.parser')
#     data=c.find_all("td",class_='nfo')
#     for d in data:
#         if 'data-spec' in d.attrs:
#             features[e][d['data-spec']]=d.text.strip()
#             # print(d['data-spec'],":",d.text.strip())
#     time.sleep(15)

# z=pd.DataFrame(features)
# z.to_csv('comparacion.csv')