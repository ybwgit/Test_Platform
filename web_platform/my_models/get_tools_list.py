from web_platform.models import my_tools


def get_tools_list():
    tools=my_tools.objects.filter()
    tools_list=[]
    for x in tools:
        one_tools={}
        one_tools['tools_name']=x.tools_name
        one_tools['tools_address']=x.tools_address
        one_tools['id']=x.id
        tools_list.append(one_tools)
    return  tools_list