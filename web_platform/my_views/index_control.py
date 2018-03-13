from django.shortcuts import render,HttpResponse
from  web_platform.my_models.get_basic_data import get_basic_data
from  web_platform.models import *
from my_python_code.mysql.Basic_information import my_sql_link
from  my_python_code.mysql.ORM_of_mysql import orm_to_mysql
import pymysql,time
def index_control(request):
    context = get_basic_data()
    a=orm_to_mysql(mysql_link=my_sql_link())
    context["my_case_of_text_total"]=a.table("web_platform_my_case_of_text").select('count(id)').all()[0]['count(id)']
    context["my_case_of_api_total"]=a.table("web_platform_my_case_of_api").select('count(id)').all()[0]['count(id)']
    context["my_case_of_ui_total"]=a.table("web_platform_my_case_of_ui").select('count(id)').all()[0]['count(id)']
    context['my_project_total']=a.table("web_platform_my_project").select('count(id)').all()[0]['count(id)']
    daily_report=[]
    for x in range(10):
        daily_report_oneday=[]
        up_time=str(time.strftime('%Y-%m-%d', time.localtime(time.time() - x * 86400))) + ' 23:59:59'
        dow_time=str(time.strftime('%Y-%m-%d',time.localtime(time.time()-x*86400)))+' 00:00:01'
        moonday=time.strftime('%Y-%m-%d',time.localtime(time.time()-x*86400))
        report_total=a.table("web_platform_my_report").select('count(id)', create_time__LT=up_time,create_time__GT=dow_time).all()[0]['count(id)']
        pass_report_total=a.table("web_platform_my_report").select('count(id)', report_result=1,create_time__LT=up_time,create_time__GT=dow_time).all()[0]['count(id)']
        failure_report_total=a.table("web_platform_my_report").select('count(id)', report_result=0,create_time__LT=up_time,create_time__GT=dow_time).all()[0]['count(id)']
        #moonday= time.mktime(time.strptime(moonday, "%Y-%m-%d"))
        daily_report.append({'moonday':'\''+moonday+'\'' ,'report_total':int(report_total),'pass_report_total':int(pass_report_total),'failure_report_total':int(failure_report_total)})
    print(daily_report)
    context['daily_report']=daily_report
    return render(request, 'index.html', context)
