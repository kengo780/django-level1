from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import Work01Form

class Work01(FormView) :
    template_name = "chapter10/work01.html"
    form_class = Work01Form
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["title"] = "Work01"
        context["sub_title"] = "フォームビュークラスです"
        return context

    def get(self, request, **kwargs) :
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
    def post(self, request, **kwargs) :
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
class Work02(FormView) :
    template_name = "chapter10/work02.html"
    form_class = Work01Form
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["title"] = "Work02"
        context["message"] = "ご入力ください"
        return context
    
    def form_valid(self, form) :
        context = self.get_context_data(**self.kwargs)
        context["message"] = "ご入力ありがとうございます"
        return self.render_to_response(context)
    
    def form_invalid(self, form) :
        context = self.get_context_data(**self.kwargs)
        context["message"] = "入力内容に誤りがあります"
        return self.render_to_response(context)

class Work03(FormView) :
    template_name = "chapter10/work03.html"
    form_class = Work01Form
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["title"] = "Work03"
        context["message"] = "ご入力ください"
        return context
    
    def form_valid(self, form) :
        context = self.get_context_data(**self.kwargs)
        context["message"] = "ご入力ありがとうございます"
        return render(self.request, "chapter11/work01thanks.html", context)