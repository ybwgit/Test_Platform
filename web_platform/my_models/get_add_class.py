from web_platform.models import course
def get_course_name():
    a = course.objects.filter()
    course_code_list=[]
    for x in a:
        course_code_list.append(x.name)
    return course_code_list
def get_course_code(name):
    a = course.objects.filter(name=name)
    course_code_list=[]
    for x in a:
        course_code_list.append(x.course_code)
        course_code_list.append(x.subject_show_id)

    return course_code_list