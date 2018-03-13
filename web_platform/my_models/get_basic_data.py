from web_platform.my_models.get_my_project import get_my_project
#基础的数据放这里，每个页面都要用到的
from  web_platform.my_models.get_tools_list import get_tools_list
from web_platform.my_models.get_task import get_task_queue

def get_basic_data():
    context={}
    context = get_task_queue(context)
    context['my_project'] = get_my_project()
    context['my_tools']=get_tools_list()
    return context