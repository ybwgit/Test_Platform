from web_platform.models import my_project
#获取当前的项目列表
def get_my_project():
    conn=my_project.objects.filter()
    project_list=[]
    for x in conn:
        one_project={}
        one_project['project_name']=x.project_name
        one_project['project_address']=x.project_address
        one_project['id']=x.id
        project_list.append(one_project)
    return  project_list