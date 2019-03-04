from django.urls import path
from django.contrib import admin

from . import views


urlpatterns = [
    path('house/', views.HouseApiView.as_view(), name='list'),
    path('house/<int:pk>/',views.HouseDetailAPIView.as_view(), name='detail'),

    path('housee/', views.customers_list),
    path('housee/<int:pk>/', views.customers_detail), 
    
]