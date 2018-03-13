from django.contrib import messages
from django.shortcuts import render
from  web_platform.my_models.get_basic_data import get_basic_data
from  web_platform.my_models.get_report import get_report,get_maxid

def report_control(request):
    id = get_maxid()
    context = get_basic_data()
    if request.method == 'GET':
            get_id = request.GET.get("id")
            if get_id:
                id=get_id
    context = get_report(context,id)
    return render(request, 'report.html', context)