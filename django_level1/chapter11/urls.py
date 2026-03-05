from django.urls import path
from . import views

app_name = 'chapter11'

urlpatterns = [
    path('work01/', views.Work01.as_view(), name='work01'),
]