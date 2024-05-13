
from django.urls import path,include
from .views import add_parking,home
urlpatterns = [
    path('', home , name="home"),
    path('add_parking',add_parking,name="main")
]
