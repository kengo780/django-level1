from django.urls import path
from . import views

app_name = "chapter02"

urlpatterns =  [
    path('hello/', views.hello, name="hello"),
]