from my_python_code.basic_information.devices_info import get_devices_info_Android
from web_platform.my_models.get_devices_Android import get_devices_info
from  web_platform.my_models.get_basic_data import get_basic_data
from web_platform.models import devices_phone
from django.shortcuts import render
def get_devices_control(request):
    context = get_basic_data()
    if request.method == 'POST':
        Android_devices_list = request.POST.getlist("Android")
        iOS_devices_list = request.POST.getlist("iOS")
        if Android_devices_list:
            for uid in Android_devices_list:
                print(uid)
                devices_phone.objects.filter(deviceName=uid).update(used='1')
        elif iOS_devices_list:
            for uid in iOS_devices_list:
                devices_phone.objects.filter(deviceName=uid).update(used='1')

        context['Android'] = get_devices_info('Android')
        context['iOS'] = get_devices_info('iOS')
        return render(request, 'task.html', context)
    else:
        devices_phone.objects.filter().delete()
        #  requests.post(url='http://127.0.0.1:8080/job/my_python_code/build?token=123456') 这个是用jenkins更新
        get_devices_info_Android()  # 本机使用这个更新数据库的连接信息
        context['Android'] = get_devices_info('Android')
        context['iOS'] = get_devices_info('iOS')
        return render(request, 'devices_phone.html', context)