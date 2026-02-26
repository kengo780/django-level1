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