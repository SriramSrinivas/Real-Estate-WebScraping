from rest_framework import serializers
from appraisal.models import Customer

from django.urls import NoReverseMatch
class customerSerializers(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    customerName=serializers.CharField(max_length=1000)
    customerEmail=serializers.EmailField()
    customerPhone=serializers.CharField()
    def create(self,validated_data):
        return Customer(**validated_data)
    def update(self,instance, validated_data):
        instance.customerName=validated_data.get('CustomerName',instance.customerName)
        instance.customerEmail=validated_data.get('CustomerEmail',instance.customerEmail)
        instance.customerPhone=validated_data.get('CustomerPhone',instance.customerPhone)

