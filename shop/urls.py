from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('cart/price', views.cart_price, name="cart_price"),
]
