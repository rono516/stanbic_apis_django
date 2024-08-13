from django.urls import path
from . import views

urlpatterns = [
    path("get_token", views.get_auth_token),
    path("pesalink", views.pesalink, name="pesalink"),
    path("rtgs", views.rtgs, name="rtgs"),
    path("swift_payment", views.swift_payment, name="swift"),
    path("paypal_pay", views.paypal_pay),
    path("checkout", views.checkout_paypal), #open page to send to paypal checkout
    path("success", views.payment_successfull, name="payment-success"),
    path("failed", views.payment_failed, name="payment-fail"),
    # path("send_to_mobile_money", views.send_to_mobile_money),
]