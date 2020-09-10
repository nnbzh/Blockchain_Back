from django.urls import path

from api import views

urlpatterns = [
    path('ethereum/', views.get_eth),
    path('ethereum/classic/', views.get_etc)
]