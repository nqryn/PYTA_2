"""
Fisier local de urls, fiecare app o sa aiba cate unul.
Dupa ce definim aici endpoints, le importam in fisierul global,
care este mysite/urls.py.

"""
from django.urls import path

from . import views

"""
Intotdeauna vom avea o lista de tipul urlpatterns,
in care vom apela functia 
path("<url relativ>", <view>, <nume view>)
"""
urlpatterns = [
    path("", views.index, name="index"),
    path("hello", views.hello, name="hello")
]