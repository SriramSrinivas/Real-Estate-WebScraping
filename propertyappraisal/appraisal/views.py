from django.shortcuts import render
from appraisal.customerSerializers import customerSerializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from appraisal.models import Customer
from rest_framework.response import Response
# from rest_framework_json_api.renderers import JsonApiRenderer
# from django.urls import NoReverseMatch
# Create your views here.
class customerList(APIView):
    # renderer_classes = (JsonApiRenderer, )
    def get(self, request,format=None):
        snippets=Customer.objects.all()
        serializer=customerSerializers(snippets,many=True)
        return Response(serializer.data)