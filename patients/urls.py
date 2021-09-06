from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.patient_list, name="list"),
    path('create/', views.patient_create, name="create"),
    path('<slug:slug>/', views.patient_detail, name="detail"),
]