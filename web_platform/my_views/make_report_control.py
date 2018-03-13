from  my_python_code.tools.add_class import add_class
from  web_platform.my_models.get_basic_data import get_basic_data
from web_platform.my_models.get_add_class import get_course_code,get_course_name
import time
from my_python_code.tools.make_report import make_report
from django.contrib import messages
from django.shortcuts import render
def make_rerort(request):
    context = get_basic_data()
    context['course_code'] = get_course_name()
    context['course_time'] = range(1, 12)
    if request.method == 'POST':#if request.method == "POST" 空的也ok  if request.POST 不能是空的
        course_code=request.POST.get("course_code")
        course_time = request.POST.get("course_time")
        class_id=request.POST.get("class_id")
        assert  int(class_id)>10000,'class_id输入错误'
        course_code_list=get_course_code(course_code)
        subject_show_id=course_code_list[1]
        course_code=str(course_code_list[0])+str(course_time)
        report_url=make_report(class_id, course_code, subject_show_id, dict_index='3', user='15600905550',password='123456')['classReportList']
        context['report_url_data'] = report_url
        print(report_url)
        if report_url:
            context['ruesl'] = 'ok'
        else:
            context['ruesl'] = 'not'
    return render(request,'make_rerort.html',context)