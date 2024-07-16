from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.subscriptionListView, name='subscription-list'),
    path('<int:pk>/', views.subscriptionDetailView, name='subscription-detail'),
]