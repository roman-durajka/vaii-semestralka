from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('cart/price', views.cart_price, name="cart_price"),
    path('cart/add/<int:product_id>', views.cart_add, name="cart_add"),
    path('cart/remove/<int:product_id>', views.cart_remove, name="cart_remove"),
]
