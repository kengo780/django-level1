from django.urls import path
from . import views

app_name = "chapter04"

urlpatterns = [
    path('work01/', views.work01, name="work01"),
    path('work02/', views.work02, name="work02"),
    path('work03/', views.work03, name="work03"),
    path('work04/', views.work04, name="work04"),
    path('work05/', views.work05, name="work05"),
    path('work06/', views.work06, name="work06"),
    path('work07/', views.work07, name="work07"),
]