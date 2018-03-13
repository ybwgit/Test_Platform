from django.shortcuts import render,HttpResponse
from  web_platform.my_models.get_basic_data import get_basic_data
from web_platform.models import *
from web_platform.my_models.get_task import get_cast_list_of_API,get_cast_list_of_UI,put_to_task_management,get_task_queue
from web_platform.my_models.my_case_of_text import get_cast_text
from my_python_code.basic_configuration.configuration_file import *
import re
def project_control(request):
    context = get_basic_data()
    if request.method == 'GET':
        if  "the_project_name" not  in  context.keys() :
            the_project_name=request.GET.get("the_project_name")
            context['the_project_name'] = the_project_name

  #  print(context)
    if request.method == 'POST':  # if request.method == "POST" 空的也ok  if request.POST 不能是空的
        add_api_case=request.POST.get("add_api_case")
        add_text_case=request.POST.get("add_text_case")
        look_source_file=request.POST.get("look_source_file")
        ui_look_source_file=request.POST.get("ui_look_source_file")
        case_data=request.POST.get("case_data")
        updata_path=request.POST.get("updata_path")
        the_project_name=request.POST.get("the_project_name")
        if  the_project_name :
            context['the_project_name'] = the_project_name
       # print(case_data,updata_path)
        if  case_data:
            case_data=case_data.replace('\r\n\r\n', '\r\n') #很重要，不知道为什么保存的时候会有换行符
            with open(updata_path, 'w',encoding='utf-8') as f:
                f.writelines(case_data)

        if ui_look_source_file:
            print('look_source_file', ui_look_source_file)
            look_source_file = eval(ui_look_source_file)
            name_url = str(look_source_file[4]).replace('.', '\\')
            print('name_url', name_url)
            my_apicase_path_1 = my_appium_path.replace('.', '\\')
            file_path = str(Complete_path + my_apicase_path_1 + '\\' + look_source_file[1] + '\\' + name_url + '\\' + str(
                look_source_file[3] + '.py'))
            print(file_path)
            with open(file_path, encoding='utf-8') as f:
                context['look_source_file'] = f.read()
            context['file_path'] = file_path
            print(context['file_path'])
        elif look_source_file:
           # context['look_source_file'] = open(r'F:\automatedTests_of_coachPadApp\appium_coachPad\test_case\正常上课.py', encoding='utf-8').read()
            print('look_source_file', look_source_file)
            look_source_file=eval(look_source_file)
            name_url=str(look_source_file[4]).replace('.','\\')
            print('name_url',name_url)
            my_apicase_path_1=my_apicase_path.replace('.','\\')
            file_path=str(Complete_path+my_apicase_path_1+'\\'+look_source_file[1]+'\\'+name_url+'\\'+str(look_source_file[3]+'.py'))
            print(file_path)
            with open(file_path,encoding='utf-8') as f:
                context['look_source_file']=f.read()
            context['file_path']=file_path
        elif add_api_case == "add_ui_case":
            case_id = request.POST.get("case_id")
            project_name = request.POST.get("project_name")
            module_name = request.POST.get("module_name")
            case_name = request.POST.get("case_name")
            case_address = request.POST.get("case_address")
            App_version = request.POST.get("App_version")
            my_case_of_text_id = request.POST.get("my_case_of_text_id")
            print(case_id,project_name,module_name,case_name,case_address,App_version,my_case_of_text_id)
            if case_id:
                nowcase = my_case_of_UI(id=case_id, project_name=project_name, module_name=module_name,case_name=case_name, case_address=case_address,App_version=App_version,my_case_of_text_id=my_case_of_text_id)
            else:
                nowcase = my_case_of_UI(project_name=project_name, module_name=module_name, case_name=case_name, case_address=case_address, App_version=App_version,my_case_of_text_id=my_case_of_text_id)
            nowcase.save()


        elif  add_api_case=="add_api_case":
            case_id=request.POST.get("case_id")
            project_name=request.POST.get("project_name")
            module_name=request.POST.get("module_name")
            api_name=request.POST.get("api_name")
            case_name=request.POST.get("case_name")
            case_address=request.POST.get("case_address")
            App_version=request.POST.get("App_version")
            if case_id:
                nowcase=my_case_of_API(id=case_id,project_name=project_name,module_name=module_name,api_name=api_name,case_name=case_name,case_address=case_address,App_version=App_version)
            else:
                nowcase =my_case_of_API(project_name=project_name,module_name=module_name,api_name=api_name,case_name=case_name,case_address=case_address,App_version=App_version)
            nowcase.save()
        elif  add_text_case:
            text_case_id = request.POST.get("text_case_id")
            text_project_name = request.POST.get("text_project_name")
            text_module_name = request.POST.get("text_module_name")
            text_case_name = request.POST.get("text_case_name")
            text_operation_steps = request.POST.get("text_operation_steps")
            text_expected_results = request.POST.get("text_expected_results")
            text_remarks = request.POST.get("text_remarks")
            text_App_version = request.POST.get("text_App_version")
            text_script_type = request.POST.get("text_script_type")
            text_script_address = request.POST.get("text_script_address")
           # print(text_operation_steps,text_expected_results)
            if add_text_case=="add_text_case":
                if  text_case_id:
                    now_text_case=my_case_of_text(id=text_case_id,
                                                  project_name=text_project_name,
                                                  module_name=text_module_name,
                                                  case_name=text_case_name,
                                                  operation_steps=text_operation_steps,
                                                  expected_results=text_expected_results,
                                                  remarks=text_remarks,
                                                  App_version=text_App_version,
                                                  script_type=text_script_type,
                                                  script_address=text_script_address,
                                                  revise_type=1,
                                                  )
                    now_text_case.save()
                else:
                    now_text_case = my_case_of_text(
                        project_name=text_project_name,
                        module_name=text_module_name,
                        case_name=text_case_name,
                        operation_steps=text_operation_steps,
                        expected_results=text_expected_results,
                        remarks=text_remarks,
                        App_version=text_App_version,
                        script_type=text_script_type,
                        script_address=text_script_address,
                        revise_type=0,
                    )
                    now_text_case.save()
            if  add_text_case=="now_add_text_case":
                if text_case_id :
                        now_text_case = my_case_of_text(id=text_case_id,
                                                        project_name=text_project_name,
                                                        module_name=text_module_name,
                                                        case_name=text_case_name,
                                                        operation_steps=text_operation_steps,
                                                        expected_results=text_expected_results,
                                                        remarks=text_remarks,
                                                        App_version=text_App_version,
                                                        script_type=text_script_type,
                                                        script_address=text_script_address,
                                                        revise_type=0,
                                                        )
                        now_text_case.save()
                else:
                    now_text_case = my_case_of_text(
                                                    project_name=text_project_name,
                                                    module_name=text_module_name,
                                                    case_name=text_case_name,
                                                    operation_steps=text_operation_steps,
                                                    expected_results=text_expected_results,
                                                    remarks=text_remarks,
                                                    App_version=text_App_version,
                                                    script_type=text_script_type,
                                                    script_address=text_script_address,
                                                    revise_type=0,
                                                    )
                    now_text_case.save()
    context = get_cast_list_of_API(context)
    context = get_cast_text(context)
    context = get_cast_list_of_UI(context)
    return render(request, 'project.html', context)