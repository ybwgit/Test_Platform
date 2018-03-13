from  my_python_code.tools.add_class import add_class
from  web_platform.my_models.get_basic_data import get_basic_data
from web_platform.my_models.get_add_class import get_course_code,get_course_name
import time
from django.contrib import messages
from django.shortcuts import render



def add_classes(request):
    context = get_basic_data()
    context['store_name'] = ['北京快快减肥通州','北京快快减肥贝蒂安店(天鹅湾)','上海亚都国际名园七星旗舰店','上海快快减肥明翼舞蹈花木店','上海快快减肥明翼舞蹈源深店','廊坊快快减肥店','广州快快减肥富力桃园店','北京望京六佰本店','北京丰台区宋家庄店','北京朝阳区优士阁店','北京朝阳区星源国际店','北京昌平区龙德紫金店','北京朝阳区常营店','北京朝阳区后现代城店','福州东二环泰禾店',]
    context['user_number'] = range(1, 15)
    context['classes_checkin_number'] = range(1, 15)
    context['course_code'] = get_course_name()
    context['course_time'] = range(1, 38)
    context['now_time_day'] = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
    context['now_time_h']=str(time.strftime('%H:%M',time.localtime(time.time())))
    print(context['now_time_day'])
    if request.method == 'POST':#if request.method == "POST" 空的也ok  if request.POST 不能是空的
        store_name=request.POST.get("store_name")
        print(store_name)
        day=request.POST.get("day")
        up_time=request.POST.get("up_time")
        course_code=request.POST.get("course_code")
        user_number=request.POST.get("user_number")
        course_time=request.POST.get("course_time")
        user_index=request.POST.get("user_index")
        classes_checkin_number=request.POST.get("classes_checkin_number")
        timeArray = time.strptime(day+' '+up_time, "%Y-%m-%d %H:%M")
        star_time = time.mktime(timeArray)
        course_code_list=get_course_code(course_code)
        subject_show_id=course_code_list[1]
        course_code=str(course_code_list[0])+str(course_time)

        class_id=add_class(star_time, store_name, user_number, classes_checkin_number, course_code, subject_show_id,user_index)
        #class_id='1111'
        messages.add_message(request, messages.INFO, class_id)
        context['class_id'] = str(class_id)
        if class_id:
            context['ruesl'] = 'ok'
        else:
            context['ruesl'] = 'not'

            #messages.success(request,class_id)
      #  return render(request,'pop.html',context)
        context['class_id'] = class_id
        #return render(request, 'add_class.html', context)
   # else:
    return render(request,'add_class.html',context)