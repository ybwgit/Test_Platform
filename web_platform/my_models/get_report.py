from web_platform.models import my_report

def get_maxid():
    a=my_report.objects.all().order_by("-id")[:2]

    for  x in a:
            return x.id

def get_report(context,id):
    a = my_report.objects.get(id=id)
    report_data=a.report_data
    report_data=eval(report_data)
    context['completion_rate'] = report_data['completion_rate']  # 终端完成率
    context['pass_tate'] = report_data['pass_tate']  # 通过率
    context['failure_rate'] = report_data['failure_rate']   # 失败率
    context['Collapse_rate'] = report_data['Collapse_rate']  # 崩溃率
    context['test_case_result']=report_data['test_case_result']
    context['App_name']=a.App_name
    context['App_version'] = a.App_version
    context['test_type']=a.test_type
    context['terminal_number']=a.terminal_number
    context['create_time']=a.create_time
    context['report_result']=a.report_result
    return context

def get_all_report(context):
    all_report = my_report.objects.all().order_by("-id")[:10]
    report_list=[]
    for  a  in all_report:
        report_one=[]
        report_one.append(a.create_time)
        report_one.append(a.App_name)
        report_one.append(a.App_version)
        report_one.append(a.test_type)
        report_one.append(a.report_result)

        if int(a.report_result)==0:
            report_one.append('未通过')
        elif int(a.report_result)==1:
            report_one.append('通过')
        report_one.append(a.id)
        report_list.append(report_one)
    context['report_list']=report_list

    return context