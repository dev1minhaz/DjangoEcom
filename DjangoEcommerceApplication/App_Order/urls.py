from django.urls import path
from. import views

app_name="App_Order"
urlpatterns = [
    path('add/<pk>/',views.add_to_cart,name="add"),
]