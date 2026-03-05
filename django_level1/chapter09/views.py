from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import Work04Form

# Create your views here.
class Work01(TemplateView) :
    template_name = "chapter09/work01.html"

class Work02(TemplateView) :
    template_name = "chapter09/work02.html"
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["title"] = "今週のニュース"
        context["sub_title"] = "規則正しい生活をしましょう"
        context["data"] = ["部活動体験","新入生歓迎会","健康診断"]
        return context
    
class Work03(TemplateView) :
    template_name = "chapter09/work03.html"
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["title"] = "部活動ニュース"
        return context
        
    def get(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        context["sub_title"] = "5月の部活動ニュース"
        context["news"] = [
            "吹奏楽部が県大会出場決定",
            "バスケ部がベスト8に進出",
            "演劇部が県大会で銀賞受賞",
        ]
        return self.render_to_response(context)
    

class Work04(TemplateView) :
    template_name = "chapter09/work04.html"
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["title"] = "年齢確認"
        context["sub_title"] = "年齢を確認します"
        return context

    def get(self, request, **kwargs) :
        context = self.get_context_data(**kwargs)
        context["form"] = Work04Form()
        return self.render_to_response(context)
    
    def post(self, request, **kwargs) :
        form = Work04Form(request.POST)
        # ageで判定
        if int(form.data["age"]) >= 18 :
            message = "選挙権があります"
        else :
            message = "選挙権がありません"
        # contextに代入
        context = self.get_context_data(**kwargs)
        context["form"] = form
        context["message"] = message
        return self.render_to_response(context)
