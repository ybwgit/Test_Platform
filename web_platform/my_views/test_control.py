from django.shortcuts import render
from  web_platform.my_models.get_basic_data import get_basic_data
from my_python_code.Operation_control.Run_case_of_api import run_api_case
def test_control(request):
    context = get_basic_data()
    run_api_case()
    if request.method == 'GET':
        a=request.GET.get("subject")
        print(a)

    return render(request, 'test.html', context)