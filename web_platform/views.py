from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from web_platform.my_views import *
from  web_platform.my_models.get_basic_data import get_basic_data
from django.contrib.auth import logout as auth_logout

@login_required
def get_devices(request):
   return get_devices_control.get_devices_control(request)

def html_test(request):
    return  test_control.test_control(request)
@login_required
def index(request):
    return index_control.index_control(request)


@login_required
def task(request):
    return task_control.task_control(request)
@login_required
def report(request):
    return  report_control.report_control(request)
@login_required
def set_up(request):
    context = get_basic_data()
    return render(request,'set_up.html',context)
@login_required
def project(request):
    return project_control.project_control(request)

def head(request):
    context = get_basic_data()
    return render(request,'head.html',context)
@login_required
def make_rerort(request):
    return make_report_control.make_rerort(request)
def add_classes(request):
    return  add_class_control. add_classes(request)
@login_required
def pop(request):
    context = get_basic_data()
    return render(request, 'pop.html', context)
def my_logon(request):
    context = get_basic_data()
    if request.method == 'POST':
        user_name=request.POST.get("user_name")
        password=request.POST.get("password")
        print(user_name,password)
        user = authenticate(username=user_name, password=password)
        if user:
            login(request, user)  # 验证成功之后登录
            return render(request, 'index.html', context)
    return render(request, 'my_logon.html', context)

def logout(request):
    context = get_basic_data()
    auth_logout(request)
    return HttpResponseRedirect('my_logon',context)

def my_handler404(request):
    context = get_basic_data()
    #auth_logout(request)
    return HttpResponseRedirect('index',context)