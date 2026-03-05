from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import Work01Form

class Work01(FormView):
    template_name = "chapter11/work01.html"
    form_class = Work01Form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "アンケートフォーム"
        context["sub_title"] = "アンケートに回答をお願いします"
        return context

    def form_valid(self, form):
        context = {
            "title": "アンケートフォーム",
            "sub_title": "アンケートに回答ありがとうございます",
            "form": form,
        }
        return render(self.request, "chapter11/work01thanks.html", context)