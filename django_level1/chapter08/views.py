from django.shortcuts import render
from .forms import Work01Form
from .forms import Work02Form
from .forms import Work03Form
from .forms import Work04Form
from .forms import Work05Form
from .forms import Work06Form
from .forms import Work07Form
from .forms import Work08Form
from .forms import Work09Form

# Create your views here.
def work01(request) :
    context = {
        "title" : "Work01",
        "form" : Work01Form()
    }
    if request.method == "POST" :
        context["form"] = Work01Form(request.POST)
    return render(request, "chapter08/work01.html", context)

def work02(request) :
    context = {
        "title" : "Work02",
        "form" : Work02Form()
    }
    if request.method == "POST" :
        context["form"] = Work02Form(request.POST)
    return render(request, "chapter08/work02.html", context)

def work03(request) :
    context = {
        "title" : "Work03",
        "form" : Work03Form()
    }
    if request.method == "POST" :
        context["form"] = Work03Form(request.POST)
    return render(request, "chapter08/work03.html", context)


def work04(request) :
    context = {
        "title" : "Work04",
        "form" : Work04Form()
    }
    if request.method == "POST" :
        context["form"] = Work04Form(request.POST)
    return render(request, "chapter08/work04.html", context)

def work05(request) :
    context = {
        "title" : "Work05",
        "form" : Work05Form()
    }
    if request.method == "POST" :
        context["form"] = Work05Form(request.POST)
    return render(request, "chapter08/work05.html", context)

def work06(request) :
    context = {
        "title" : "Work06",
        "form" : Work06Form()
    }
    if request.method == "POST" :
        context["form"] = Work06Form(request.POST)
    return render(request, "chapter08/work06.html", context)

def work07(request) :
    context = {
        "title" : "Work07",
        "form" : Work07Form()
    }
    if request.method == "POST" :
        context["form"] = Work07Form(request.POST)
    return render(request, "chapter08/work07.html", context)

def work08(request) :
    context = {
        "title" : "Work08",
        "form" : Work08Form()
    }
    if request.method == "POST" :
        context["form"] = Work08Form(request.POST)
    return render(request, "chapter08/work08.html", context)

def work09(request):
    context = {
        "title": "Work09",
        "form": Work09Form()
    }
    if request.method == "POST":
        context["form"] = Work09Form(request.POST)

    return render(request, "chapter08/work09.html", context)