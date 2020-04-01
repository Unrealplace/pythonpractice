from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {}
    print('hellow---->',request)
    context['hello'] = '大家好，欢迎来到我的世界！'
    return render(request,'hello.html',context)
    pass
