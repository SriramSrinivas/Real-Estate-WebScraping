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
from rest_framework import viewsets, filters, parsers, renderers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.authentication import *

from django.contrib.auth.models import *
from django.contrib.auth import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
#from django.shortcuts import render_to_response
from django.template import RequestContext
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, parsers, renderers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tables import CustomerTable
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.authentication import *
import requests
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
# from Scraping import WebScraping
# api = API()
# from rest_framework_json_api.renderers import JsonApiRenderer
# from django.urls import NoReverseMatch
# Create your views here.
# @api.register
def index(request):
   return render(request,'templates/intro.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'templates/signup.html', {'form': form})

def home(request):
 
   return render(request, 'templates/base.html')
@login_required
def customerListSecured(request):
    snippets=Customer.objects.all()
    return render(request,'templates/customer.html',{'snippets':snippets})

@login_required
def propertyListSecured(request):
    es = Elasticsearch(['elasticsearch:9200'])
    res = es.search(index="my-index222", body={"query": {"match_all": {}}},size=1000)
    print(res)
    print("Got %d Hits:" % res['hits']['total'])
       
    id=0
    snippets=[]
    jsonResponse=[]
    for hit in res['hits']['hits']:
        address="%(Address)s" % hit["_source"]
        price="%(price)s" % hit["_source"]
        jsonResponse.append({"id":id,"price":price,"Address":address})
        id=id+1    

    return render(request,'templates/property.html',{'snippets':jsonResponse})


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
class Session(APIView):
    permission_classes = (AllowAny,)
    def form_response(self, isauthenticated, userid, username, error=""):
        data = {
            'isauthenticated': isauthenticated,
            'userid': userid,
            'username': username
        }
        if error:
            data['message'] = error

        return Response(data)

    def get(self, request, *args, **kwargs):
        # Get the current user
        if request.user.is_authenticated():
            return self.form_response(True, request.user.id, request.user.username)
        return self.form_response(False, None, None)

    def post(self, request, *args, **kwargs):
        # Login
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return self.form_response(True, user.id, user.username)
            return self.form_response(False, None, None, "Account is suspended")
        return self.form_response(False, None, None, "Invalid username or password")

    def delete(self, request, *args, **kwargs):
        # Logout
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)