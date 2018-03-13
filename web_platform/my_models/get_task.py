from  web_platform.models import my_case_of_API,task_management,my_case_of_UI
from web_platform.my_models.get_my_project import get_my_project
import uuid,time
from datetime import datetime

def get_cast_list_of_API(context):
    context['case_list']={}
    my_project = get_my_project()
    project_list=[]
    for x in my_project:
        project_list.append(x['project_name'])
    for y in  project_list:
        project_case=my_case_of_API.objects.filter(project_name=y)
        case_all=[]
        api_name_list=[]
        for z in project_case:
            case_one=[]
            case_one.append(z.id)
            if z.module_name not in api_name_list:
                api_name_list.append(z.module_name)
            case_one.append( z.project_name)
            case_one.append(z.api_name)
            case_one.append(z.case_name)
            case_one.append(z.case_address)
            case_one.append(z.module_name)
            case_all.append(case_one)
        context['case_list'][y]=[api_name_list,case_all]
    return context


def get_cast_list_of_UI(context):
    context['UI_case_list']={}
    my_project = get_my_project()
    project_list=[]
    for x in my_project:
        project_list.append(x['project_name'])
    for y in  project_list:
        project_case=my_case_of_UI.objects.filter(project_name=y)
        case_all=[]
        module_name_list=[]
        for z in project_case:
            case_one=[]
            case_one.append(z.id)
            if z.module_name not in module_name_list:
                module_name_list.append(z.module_name)
            case_one.append( z.project_name)
            case_one.append(z.module_name)
            case_one.append(z.case_name)
            case_one.append(z.case_address)
            case_one.append(z.App_version)
            case_one.append(z.my_case_of_text_id)
            case_all.append(case_one)
        context['UI_case_list'][y]=[module_name_list,case_all]
    return context

def put_to_task_management(task_json):
        now_data=task_management(task_project=task_json['project_name'],task_uuid=uuid.uuid4(),task_state=task_json['task_state'],task_type=task_json['test_type'],task_data={'case_list':task_json["case_list"]},create_time=task_json["todaytime"])
        now_data.save()
        return 1

def get_task_queue(context):
    get_now_task=task_management.objects.filter(task_state__lt=2).order_by("-id")[:10]
    print(get_now_task)
    task_all=[]
    for x in get_now_task:
        task_one=[]
        task_one.append(x.task_type)
        task_one.append(x.task_project)
        task_one.append(x.task_state)
        task_one.append(x.create_time)
        task_one.append(x.task_data)
        task_all.append(task_one)
    context['task_state_list'] = task_all
    return context
def get_task_queue_custom(context,task_type_custom,task_state_custom):
    now_time = datetime.fromtimestamp(time.time())
    get_now_task=task_management.objects.filter(task_type=task_type_custom,task_state=task_state_custom,create_time__lte=now_time).order_by("-id")
    #print(get_now_task)
    task_all=[]
    for x in get_now_task:
        task_one=[]
        task_one.append(x.id)
        task_one.append(x.task_type)
        task_one.append(x.task_project)
        task_one.append(x.task_state)
        task_one.append(x.create_time)
        task_one.append(x.task_data)
        task_one.append(x.task_uuid)
        task_all.append(task_one)
    context['task_state_list'] = task_all
    return context

if __name__ == '__main__':
    context={}

    get_cast_list(context)
