from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cart/", views.cart, name="cart"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login")
]
