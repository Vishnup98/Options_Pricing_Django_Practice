from django.urls import path
from django.contrib import admin
from django.urls import include,path



from . import views

app_name="options"
urlpatterns = [
    path('', views.index, name='index'),
    path("price/Option<int:option_id>/",views.price,name="price"),
]

