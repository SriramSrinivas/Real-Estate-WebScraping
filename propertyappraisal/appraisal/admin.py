from django.contrib import admin
from appraisal.models import Customer
class customerlist(admin.ModelAdmin):
    list_display=('customerName','customerEmail','customerPhone')
    
admin.site.register(Customer,customerlist)

