from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('about/', views.about, name="about"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

]
