from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('cart/update', views.cart_info, name="cart_info"),
    path('cart/update/quantity/', views.update_quantity, name="update_quantity"),
    path('cart/add/', views.cart_add, name="cart_add"),
    path('cart/remove/', views.cart_remove, name="cart_remove"),
    path('cart/submit/', views.submit_cart, name="submit_cart"),
]
