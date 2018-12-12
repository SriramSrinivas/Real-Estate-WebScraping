from django.shortcuts import render
from appraisal.customerSerializers import customerSerializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from appraisal.models import Customer
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
        doc = {
        'size' : 10000,
        'query': {
            'match_all' : {}
            }
        }
        res = es.search(index='my-index1', doc_type='test-type', body=doc,scroll='1m')

        scroll = res['_scroll_id']
        print(scroll)
         
        snippets=Customer.objects.all()
        serializer=customerSerializers(snippets,many=True)
        return Response(serializer.data)
