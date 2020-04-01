from django.http import HttpResponse
from django.shortcuts import render

def search(request):

    if 'name' in request.GET and request.GET['name']:
        message = '你的搜索内容为：' + request.GET['name']
    else:
        message = '你提交了空的表单'

    return HttpResponse(message)
    pass

def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['name']
    return render(request,'search_post_form.html',ctx)
    pass

def search_form(request):
    return render(request,'search_form.html')
    pass
