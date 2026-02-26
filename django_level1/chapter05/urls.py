from django.urls import path
from . import views

app_name = "chapter05"

urlpatterns = [
    path('work01/', views.work01, name="work01"),
    path('work02/', views.work02, name="work02"),
    path('work03a/', views.work03a, name="work03a"),
    path('work03b/', views.work03b, name="work03b"),
    path('work04a/', views.work04a, name="work04a"),
    path('work04b/', views.work04b, name="work04b"),
    path('work05a/', views.work05a, name="work05a"),
    path('work05b/', views.work05b, name="work05b"),
    path('work06/', views.work06, name="work06"),
    path('work07/', views.work07, name="work07"),
    path('work08/<str:name>', views.work08, name="work08"),
    path('work09/<str:name>/<int:age>', views.work09, name="work09"),
    path('work10/', views.work10, name="work10"),
    path('work11/', views.work11, name="work11"),
]