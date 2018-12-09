import urllib.request
from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
from elasticsearch import Elasticsearch
# Fetch the html file


urls=[]
priceList=[]
AddressList=[]
propertyDictionary={}
total=0
es = Elasticsearch()
# es.indices.create(index='my-index1',ignore=400)
urls=['https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/?sortbyfield=proximity,asc&itemsper=50']
while True:
    # es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
    for x in urls:
        response = requests.get(x)
        # print(response.content)
        
        # print(response.read())
        html_doc = response.content

# # Parse the html file
        soup = BeautifulSoup(html_doc, "html.parser")

# # Format the parsed html file
        strhtm =soup.prettify("utf-8")
        # with open("test.html","w") as file:
        #      file.write(str(strhtm))
        for x in soup.findAll("dd",{"class":"price"}):
            y=str(x)
            z=y.split("$")
            m=z[1].split("</dd>")
            
            priceList.append("Price:"+m[0])
        for x in soup.findAll("span",{"itemprop":"streetAddress"}):
            y=str(x)
            z=y.split("streetAddress")
            m=z[1].split(">")
            k=m[1].split("</span")
            print(k[0])
            AddressList.append("Address:"+k[0])
    i=0
    for x,y in zip(priceList,AddressList):
        propertyDictionary[i]=x,y
       
        i=i+1
    print(propertyDictionary)
    print('done')
    time.sleep(500)
