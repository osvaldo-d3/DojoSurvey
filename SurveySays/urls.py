from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('form/', views.form),
    path('add-new/', views.newMembers),
    path('results/', views.results),
    path('ninjcoin/', views.theCoin),
    path('reset/', views.reset),
    path('purchase/', views.purchase)
]