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
i=0
id=1
es = Elasticsearch()
# es.indices.create(index='my-index1')
urls=['https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/?sortbyfield=proximity,asc&itemsper=50','https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-2/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-3/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-4/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-5/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-6/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-7/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-8/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-9/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-10/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-11/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-12/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-13/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-14/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-15/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-16/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-17/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-18/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-19/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-20/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-21/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-22/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-23/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-24/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-25/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-26/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-27/?sortbyfield=featured,desc&itemsper=50',
'https://www.realtytrac.com/mapsearch/sold/ne/sarpy-county/p-28/?sortbyfield=featured,desc&itemsper=50'


]
while True:
    this={}
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
            priceList.append(m[0])
            
        for x in soup.findAll("span",{"itemprop":"streetAddress"}):
            y=str(x)
            z=y.split("streetAddress")
            m=z[1].split(">")
            k=m[1].split("</span")
            # print(k[0])
            AddressList.append(k[0])
            
     
    for x,y in zip(priceList,AddressList):
        this={"price":x,
              "Address":y}
        print(this)
        es.index(index="my-index1", doc_type="test-type", id=id, body=this)
        # propertyDictionary[i]=x,y
        id=id+1
    # print(propertyDictionary)
    id=1
    # es.index(index="my-index1", doc_type="test-type", id=id, body=propertyDictionary)
    # id=id+1
   
    # print(propertyDictionary)
    # for x,y in propertyDictionary.items():
    #     this={x,y}
    #     print(this)
    #     es.index(index="my-index1", doc_type="test-type", id=id, body=this)
    #     id=id+1
    print('done')
    time.sleep(500)
