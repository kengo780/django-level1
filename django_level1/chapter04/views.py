from django.shortcuts import render

# Create your views here.
def work01(request):
    return render(request, "chapter04/work01.html")

def work02(request):
    context = {
        "title" : "ワーク2",
        "message" : "私は名前は佐藤です",
    }
    return render(request, "chapter04/work02.html", context)

def work03(request):
    context = {
        "title" : "都市",
        "city" : ["東京", "ニューヨーク", "ロンドン", "パリ", "マドリード"],
    }
    return render(request, "chapter04/work03.html", context)    

def work04(request):
    context = {
        "title" : "国名と首都",
        "nations" : {
            "日本" : "東京",
            "イギリス" : "ロンドン",
            "フランス" : "パリ",
            "アメリカ" : "ワシントンDC",
        },
    }
    return render(request, "chapter04/work04.html", context)    


def work05(request):
    context = {
        "title" : "月",
        "data" : {
            "January" : "1月",
            "February" : "2月",
            "March" : "3月",
            "April" : "4月",
            "May" : "5月",
        }
    }
    return render(request, "chapter04/work05.html", context)   

def work06(request):
    context = {
        "title" : "好きな映画",
        "movie" : ["ハリーポッター", "美女と野獣", "スターウォーズ"],
    }
    return render(request, "chapter04/work06.html", context)


def work07(request):
    context = {
        "title" : "期末試験の成績",
        "scores" : {
            "国語" : 90,
            "数学" : 92,
            "英語" : 85,
            "理科" : 94,
            "社会" : 80,
        }
    }
    return render(request, "chapter04/work07.html", context)