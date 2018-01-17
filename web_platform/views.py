from django.shortcuts import render
import requests
from web_platform.models import devices_phone
from web_platform.python.get_devices_Android import get_devices_info

def get_devices(request):
    context={}
    requests.post(url='http://127.0.0.1:8080/job/my_python_code/build?token=123456')
    context['Android'] = get_devices_info('Android')
    context['iOS'] = get_devices_info('iOS')
    return render(request,'devices_phone.html',context)
def html_test(request):
    context={}
   # context['data'] = get_devices_info()
    return render(request,'test.html',context)
def index(request):
    context={}
    return render(request,'index.html',context)
def task(request):
    context={}
    return render(request,'task.html',context)
def report(request):
    context={}
    return render(request,'report.html',context)
def set_up(request):
    context={}
    return render(request,'set_up.html',context)