from  web_platform.models import  my_case_of_text
from web_platform.my_models.get_my_project import get_my_project

def get_cast_text(context):
    context['text_case_list']={}
    my_project = get_my_project()
    project_list = []
    for x in my_project:
        project_list.append(x['project_name'])
    for y in project_list:
        project_case = my_case_of_text.objects.filter(project_name=y)
        case_all = []
        api_name_list = []
        for z in project_case:
            case_one = []
            case_one.append(z.id)
            if z.module_name not in api_name_list:
                api_name_list.append(z.module_name)
            case_one.append(z.project_name)
            case_one.append(z.module_name)
            case_one.append(z.case_name)
            case_one.append(z.operation_steps)
            case_one.append(z.expected_results)
            case_one.append(z.remarks)
            case_one.append(z.App_version)
            case_one.append(z.script_type)
            case_one.append(z.script_address)
            case_all.append(case_one)
        context['text_case_list'][y] = [api_name_list, case_all]
    return context
