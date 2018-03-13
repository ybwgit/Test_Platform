"""Test_Platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from  web_platform import views
urlpatterns = [
    path(r'test', views.html_test),
    path('admin', admin.site.urls),
    path(r'index', views.index),
    path(r'devices_phone', views.get_devices),
    path(r'task', views.task),
    path(r'report', views.report),
    path(r'set_up',views.set_up),
    path(r'project',views.project),
    path(r'head',views.head),
    path(r'make_report',views.make_rerort),
    path(r'add_class',views.add_classes),
    path(r'pop',views.pop),
    path(r'my_logon/',views.my_logon),
    path(r'logout',views.logout),

]

handler404 = views.my_handler404
handler500 =   views.my_handler404