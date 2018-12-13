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
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views
# from django.core.urlresolvers import NoReverseMatch
# from api import urls 
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^customerlist/$',csrf_exempt(views.customerList.as_view())),
    url(r'^propertylist/$',csrf_exempt(views.propertyList.as_view())),
    url(r'^customer/$',csrf_exempt(views.customerListSecured)),
    # url(r'^property/$',csrf_exempt(views.propertyListSecured)),

    url(r'^session/$', csrf_exempt(views.Session.as_view())),
    url(r'^home/$', views.home),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^customers/$',controllers.test),
]
