from django.urls import path
from . import views

app_name = "chapter09"

urlpatterns = [
    path('work01/', views.Work01.as_view(), name="work01"),
    path('work02/', views.Work02.as_view(), name="work02"),
    path('work03/', views.Work03.as_view(), name="work03"),
    path('work04/', views.Work04.as_view(), name="work04"),
]