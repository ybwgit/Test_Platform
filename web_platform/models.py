from django.db import models
#这个表实际上是控制数据库的
class phone(models.Model):#这个表是记录手机的号码的
        phone_code=models.CharField(max_length=30)
class devices_phone(models.Model):#这个表是记录手机的链接信息的
    deviceName = models.CharField(max_length=30, primary_key=True)  # 主键  手机的名字
    platformName = models.CharField(max_length=30)  # 手机的平台 安卓oriOS
    platformVersion = models.CharField(max_length=30)  # 版本号
    state = models.CharField(max_length=30)  # 状态
    id=models.CharField(max_length=10)
    used=models.CharField(max_length=10)
class my_project(models.Model):
    id = models.CharField(max_length=10, primary_key=True)  # 主键
    project_name=models.CharField(max_length=30) #项目的名字
    project_address=models.CharField(max_length=30)#项目的地址

class my_report(models.Model):
        user_name=models.CharField(max_length=30) #提交的用户名称
        report_data=models.TextField()  #报告的json  大部分数据保存在这里
        report_result=models.CharField(max_length=30)  #报告的结果 成功与否
        uuid=models.CharField(max_length=100)     #报告的uuid
        create_time=models.DateTimeField(auto_now=True)  #生成时间
        App_name=models.CharField(max_length=100)  #app名
        test_type=models.CharField(max_length=30)  #测试类型
        terminal_number=models.CharField(max_length=30)  #用到了多少台手机
        App_version=models.CharField(max_length=30)  #app版本号


class  my_tools(models.Model): #小工具的列表
        tools_name=models.CharField(max_length=30) #工具名
        tools_address=models.CharField(max_length=30) #对应的网页地址

class course(models.Model):
    name=models.CharField(max_length=30)
    course_code=models.CharField(max_length=30)
    subject_show_id=models.CharField(max_length=30)
    subject_total=models.CharField(max_length=30)

class my_case_of_API(models.Model):
    project_name=models.CharField(max_length=30)
    module_name=models.CharField(max_length=30)
    api_name=models.CharField(max_length=50)
    case_name=models.CharField(max_length=100)
    case_address=models.CharField(max_length=255)
    App_version = models.CharField(max_length=255)
    my_case_of_text_id = models.CharField(max_length=255)
class my_case_of_UI(models.Model):
    project_name = models.CharField(max_length=30)
    module_name= models.CharField(max_length=30)
    case_name = models.CharField(max_length=100)
    case_address = models.CharField(max_length=255)
    App_version = models.CharField(max_length=255)
    my_case_of_text_id = models.CharField(max_length=255)
class task_management(models.Model):
    task_uuid=models.CharField(max_length=100)
    task_state=models.IntegerField() #0 未运行  1 运行中 2 运行完毕
    task_type=models.CharField(max_length=30)  #提交测试的类型 目前 appium  api测试
    task_data=models.TextField()
    task_project=models.CharField(max_length=30)
    create_time = models.DateTimeField()  # 生成时间

class  my_case_of_text(models.Model):
    project_name = models.CharField(max_length=300)
    module_name = models.CharField(max_length=300)
    case_name = models.CharField(max_length=1000)
    operation_steps= models.CharField(max_length=2550)
    expected_results=models.CharField(max_length=2550)
    remarks=models.CharField(max_length=2550)
    App_version = models.CharField(max_length=255)
    script_type = models.CharField(max_length=300)
    script_address = models.CharField(max_length=300)
    revise_type= models.CharField(max_length=300)

class user (models.Model):
    user_name = models.CharField(max_length=300)
    user_password = models.CharField(max_length=300)

class  pad_pesourceList(models.Model):
    courseCode=models.CharField(max_length=300)
    json_data=models.TextField()


