"""property URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from appraisal import controllers
from appraisal import views
# from django.core.urlresolvers import NoReverseMatch
# from api import urls 
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^customer/$',views.customerList.as_view()),
    url(r'^property/$',views.propertyList.as_view()),
    # url(r'^customers/$',controllers.test),
]
