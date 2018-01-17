from django.shortcuts import render

from web_platform.models import devices_phone
from web_platform.python.get_devices_Android import get_devices_info

def get_devices(request):
    context={}
    context['Android'] = get_devices_info('Android')
    context['iOS'] = get_devices_info('iOS')
    return render(request,'devices_phone.html',context)
def html_test(request):
    context={}
   # context['data'] = get_devices_info()
    return render(request,'test.html',context)