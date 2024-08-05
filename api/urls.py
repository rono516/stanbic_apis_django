from django.urls import path
from . import views

urlpatterns = [
    path("get_token", views.get_auth_token),
    path("make_payment", views.make_payment),
    path("rtgs", views.rtgs),
    path("swift_payment", views.swift_payment),
    path("send_to_mobile_money", views.send_to_mobile_money),
]