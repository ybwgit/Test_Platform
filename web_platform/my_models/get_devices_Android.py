#在数据库里面获取当前在线的机子
from web_platform.models import devices_phone
def get_devices_info(platform_name):
    a = devices_phone.objects.filter(platformName=platform_name)
    phone_list=[]
    for x in a:
        device_one = {}
        device_one['id']=x.id
        device_one['deviceName']=x.deviceName
        device_one['platformName']=x.platformName
        device_one['platformVersion']=x.platformVersion
        device_one['state']=x.state
        phone_list.append(device_one)
    return phone_list











if __name__ == '__main__':
    get_devices_info()
