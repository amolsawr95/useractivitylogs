"""NewProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import re_path,include
from NewApp.api.viewset import NewUserViewset
from NewApp import views as ab
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'newusers', NewUserViewset)
urlpatterns = [
    re_path(r'^$',ab.index,name='home'),
    re_path(r'newuser/$',ab.newuser,name='newuser'),
    re_path(r'^(?P<id>\d+)/activitylogs/$', ab.activity_log, name='activity_log'),
    re_path(r'^(?P<id>\d+)/activityadd/$', ab.activity_add, name='activity_add'),
    re_path(r'^api', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
