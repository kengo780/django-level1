from django.shortcuts import render

# Create your views here.
def work01(request):
    context = {
        "title" : "ワーク01",
        "links" : {
            "Youtube" : "https://www.youtube.com/",
            "Amazon" : "https://www.amazon.co.jp/",
            "Instagram" : "https://www.instagram.com/",
        }
    }
    return render(request, "chapter05/work01.html", context)

def work02(request):
    context = {
        "title" : "ワーク02",
    }
    return render(request, "chapter05/work02.html", context)


def work03a(request):
    context = {
        "title" : "ワーク03a"
    }
    return render(request, "chapter05/work03a.html", context)


def work03b(request):
    context = {
        "title" : "ワーク03b"
    }
    
    # GETパラメータの取得
    name = request.GET["name"]
    age = request.GET["age"]
    
    # GETパラメータを辞書にする
    data = {
        "name" : name,
        "age" : age,
    }
    
    # GETパラメータの代入
    context["data"] = data
    return render(request, "chapter05/work03b.html", context)

def work04a(request):
    context = {
        "title" : "ワーク04a"
    }
    return render(request, "chapter05/work04a.html", context)


def work04b(request):
    context = {
        "title" : "ワーク04b"
    }
    
    # GETパラメータの取得
    data = {}
    data["name"] = request.GET.get("name","")
    data["age"] = request.GET.get("age","");

    # GETパラメータの代入
    context["data"] = data
    return render(request, "chapter05/work04b.html", context)

def work05a(request):
    context = {
        "title" : "ワーク05a"
    }
    return render(request, "chapter05/work05a.html", context)


def work05b(request):
    context = {
        "title" : "ワーク05b"
    }
    
    # POSTパラメータの取得
    data = {}
    data["name"] = request.POST.get("name","")
    data["age"] = request.POST.get("age","")
    
    # POSTパラメータの代入
    context["data"] = data
    return render(request, "chapter05/work05b.html", context)

def work06(request):
    context = {
        "title" : "ワーク06"
    }
    
    data = {}
    if request.method == "POST" :
        # POSTパラメータの取得
        data["name"] = request.POST.get("name","")
        data["age"] = request.POST.get("age","")
    
    # 代入
    context["data"] = data
    return render(request, "chapter05/work06.html", context)

def work07(request):
    context = {
        "title" : "ワーク07"
    }

    data = {}
    if request.method == "POST" :
        # POSTパラメータの取得
        age = request.POST.get("age","")
        # 数値に変換する
        data["age"] = int(age)
    
    # 代入
    context["data"] = data
    return render(request, "chapter05/work07.html", context)


def work08(request, name):
    context = {
        "title" : "ワーク08",
        "data" : {
            "name" : name,
        },
    }
    return render(request, "chapter05/work08.html", context)

def work09(request, name, age):
    context = {
        "title" : "ワーク09",
        "data" : {
            "name" : name,
            "age" : age,
        },
    }
    return render(request, "chapter05/work09.html", context)

def work10(request):
    context = {
        "title" : "ワーク10",
    }
    # この部分を下側で「render」関数直前までを自分で作成します
    data = {}
    if request.method == "POST" :
        # POSTパラメータの取得
        data["music"] = request.POST.get("music","")
        data["movie"] = request.POST.get("movie","")
    
    # 代入
    context["data"] = data
    return render(request, "chapter05/work10.html", context)


def work11(request):
    context = {
        "title" : "ワーク11"
    }

    data = {}
    if request.method == "POST" :
        # POSTパラメータの取得
        name = request.POST.get("name","")
        score = request.POST.get("score","")
        # 数値に変換する
        data["name"] = name
        data["score"] = int(score)
    
    # 代入
    context["data"] = data
    return render(request, "chapter05/work11.html", context)