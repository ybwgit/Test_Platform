from django.db import models

class devices_phone(models.Model):
    deviceName = models.CharField(max_length=30, primary_key=True)  # 主键  手机的名字
    platformName = models.CharField(max_length=30)  # 手机的平台 安卓oriOS
    platformVersion = models.CharField(max_length=30)  # 版本号
    state = models.CharField(max_length=30)  # 状态
    id=models.CharField(max_length=10)
