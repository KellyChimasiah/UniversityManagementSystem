from django.urls import path
from . import views

urlpatterns = [
    path('fees/', views.fee_list, name='fee_list'),
    path('fees/<int:fee_id>/', views.fee_detail, name='fee_detail'),
    path('fees/<int:fee_id>/make_payment/', views.make_payment, name='make_payment'),
]