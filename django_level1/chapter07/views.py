from django.shortcuts import render

# Create your views here.
def work01(request) :
    context = {
        "title" : "今日のトップニュース",
        "sub_title" : "台風接近の予報",
    }
    return render(request,'chapter07/work01.html', context)

def work02(request) :
    context = {     
        "title" : "大ヒット映画上映中",
        "sub_title" : "歴史マンガ原作の大人気アクション映画",
    }
    return render(request,'chapter07/work02.html', context)

def work03(request) :
    context = {
        "title" : "今週の部活動スケジュール",
        "sub_title" : "中間試験前のため部活動は休みです",
    }
    return render(request,'chapter07/work03.html', context)


def work04(request) :
    context = {
        "title" : "ワーク04",
        "page_title" : "4月のスケジュール",
        "sub_title" : "部活動体験が始まります",
    }
    return render(request,'chapter07/work04.html', context)