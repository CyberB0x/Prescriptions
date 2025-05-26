from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_prescription, name='create_prescription'),
    path('<uuid:pk>/', views.prescription_detail, name='prescription_detail'),
    path('<uuid:pk>/download/', views.download_prescription_pdf, name='download_prescription_pdf'),
    path('', views.prescription_list, name='prescriptions_list'),

]
