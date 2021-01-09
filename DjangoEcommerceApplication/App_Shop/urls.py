from django.urls import path
from . import views

app_name="App_Shop"
urlpatterns = [
path('',views.Home.as_view(),name="home"),
]
