from django.urls import path
from . import views

app_name = "chapter03"

urlpatterns = [
    path('work04/', views.work04, name="work04"),
    path('work05/', views.work05, name="work05"),
    path('work06/', views.work06, name="work06"),
]