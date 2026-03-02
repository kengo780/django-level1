from django.shortcuts import render

# Create your views here.
def work01(request) :
    context = {
        "title" : "ワーク01",
    }
    data = {}
    if request.method == "POST" :
        data["name"] = request.POST.get("name","")
        data["hobby"] = request.POST.get("hobby","")
    context["data"] = data
    return render(request, "chapter06/work01.html", context)


def work02(request) :
    context = {
        "title" : "ワーク02",
    }
    data = {}
    if request.method == "POST" :
        data["city"] = request.POST.get("city","")
    context["data"] = data
    return render(request, "chapter06/work02.html", context)    

def work03(request) :
    context = {
        "title" : "ワーク03",
    }
    data = {}
    if request.method == "POST" :
        data["music"] = request.POST.get("music","")
    context["data"] = data
    return render(request, "chapter06/work03.html", context)

def work04(request) :
    context = {
        "title" : "ワーク04",
    }
    data = {}
    if request.method == "POST" :
        data["movie"] = request.POST.getlist("movie")
    context["data"] = data
    return render(request, "chapter06/work04.html", context)


def work05(request) :
    context = {
        "title" : "ワーク05",
    }
    data = {}
    if request.method == "POST" :
        data["message"] = request.POST.get("message", "")
    context["data"] = data
    return render(request, "chapter06/work05.html", context)

def work06(request) :
    context = {
        "title" : "ワーク06",
    }
    data = {}
    if request.method == "POST" :
        data["secret"] = request.POST.get("secret", "")
    context["data"] = data
    return render(request, "chapter06/work06.html", context)

def work07(request) :
    context = {
        "title" : "ワーク07",
    }
    data = {}
    if request.method == "POST" :
        data["country"] = request.POST.get("country","")
    context["data"] = data
    return render(request, "chapter06/work07.html", context)   

def work08(request) :
    context = {
        "title" : "ワーク08",
    }
    data = {}
    if request.method == "POST" :
        data["food"] = request.POST.getlist("food")
    context["data"] = data
    return render(request, "chapter06/work08.html", context)