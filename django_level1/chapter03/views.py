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

def work04(request):
    message= """
<html>
    <body>
        <h1>Fruits</h1>
            <ul>
                <li>apples</li>
                <li>orange</li>
                <li>melon</li>
            </ul>
    </body>
</html>"""
    return HttpResponse(message)

def work05(request):
    message="""
<html>
    <body>
        <h1>生徒一覧</h1>
            <ul>
                <li>ジョン</li>
                <li>ナンシー</li>
                <li>ボブ</li>
            </ul>
    </body>
</html>"""
    return HttpResponse(message)


def work06(request):
    message="""
<html>
    <body>
        <h2>今日の天気</h2>
        <h2>晴れのち曇り</h2>
        <h2>最高気温：30度</h2>P
        <h2>最低気温：21度</h2>
    </body>
</html>
"""
    return HttpResponse(message)