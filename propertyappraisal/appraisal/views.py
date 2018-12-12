from django.shortcuts import render
from appraisal.customerSerializers import customerSerializers
from appraisal.customerSerializers import propertySerializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from appraisal.models import Customer
from appraisal.models import Property
from rest_framework.response import Response
from jsonapi.api import API
from jsonapi.resource import Resource
from rest_framework.renderers import JSONRenderer
from elasticsearch import Elasticsearch
import time
from elasticsearch_dsl.connections import connections


# from Scraping import WebScraping
# api = API()
# from rest_framework_json_api.renderers import JsonApiRenderer
# from django.urls import NoReverseMatch
# Create your views here.
# @api.register
class customerList(APIView):
    renderer_classes = (JSONRenderer, )
    def get(self, request,format=None):
        snippets=Customer.objects.all()
        serializer=customerSerializers(snippets,many=True)
        return Response(serializer.data)
class propertyList(APIView):
    renderer_classes = (JSONRenderer, )
    def get(self,request,format=None):
       
        # time.sleep(12)
        # connections.create_connection()
        es = Elasticsearch(['elasticsearch:9200'])
        res = es.search(index="my-index222", body={"query": {"match_all": {}}},size=1000)
        print(res)
        print("Got %d Hits:" % res['hits']['total'])
        jsonResponse=[]
        id=0
        for hit in res['hits']['hits']:
            address="%(Address)s" % hit["_source"]
            price="%(price)s" % hit["_source"]
            jsonResponse.append({"id":id,"price":price,"Address":address})
            id=id+1
        serializer=propertySerializers(jsonResponse,many=True)
        return Response(serializer.data)
