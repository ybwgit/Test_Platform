from django.shortcuts import render
from  web_platform.my_models.get_basic_data import get_basic_data
from  web_platform.my_models.get_report import get_all_report
from  web_platform.my_models.get_report import get_report
from web_platform.my_models.get_task import get_cast_list_of_API,put_to_task_management,get_task_queue,get_cast_list_of_UI
import time
def task_control(request):
    context = get_basic_data()
    context=get_all_report(context)
    context=get_cast_list_of_API(context)
    context=get_cast_list_of_UI(context)
    print(context)
    context["todaytime"]= str(time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime(time.time())))
   # print(context)
    if request.method == 'POST':
        context = get_task_queue(context)
        report_index=request.POST.get('report_index')
        if report_index: #点查看报告跳转到报告页面
            context = get_report(context, int(report_index))
            return render(request, 'report.html', context)
        test_type=request.POST.get('test_type')
        context['test_type']=test_type
        selected_case_list= request.POST.getlist("selected_case_list")
        context['selected_case_list']=selected_case_list
        if selected_case_list:
            todaytime = request.POST.get('todaytime')
            todaytime=str(todaytime).replace('T',' ')
            print(11111111111, todaytime)
            project_name=request.POST.get('project_name')
            task_json={}
            task_json['task_state']=0
            task_json['test_type'] = request.POST.get('test_type1')
            task_json['project_name'] = project_name
            task_json['case_list'] = selected_case_list
            task_json["todaytime"]=todaytime
            put_to_task_management(task_json)

            context = get_basic_data()
            context = get_all_report(context)
            context = get_cast_list_of_API(context)
            context["todaytime"] = str(time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(time.time())))
            context = get_task_queue(context)
            return render(request, 'task.html', context)
    context = get_task_queue(context)
    return render(request, 'task.html', context)