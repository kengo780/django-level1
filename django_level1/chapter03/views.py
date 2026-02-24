from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def work01(request):
    message = "Hello Work01"
    return HttpResponse(message)

def work02(request):
    message = "私は名前は山田です"
    return HttpResponse(message)

def work03(request):
    message = "<html><body><h1>今日は晴天</h1></body></html>"
    return HttpResponse(message)