from django.urls import path
from django.contrib import admin

from . import views


urlpatterns = [
    path('agent/', views.HouseApiView.as_view(), name='list'),
    path('agent/<int:pk>/',views.HouseDetailAPIView.as_view(), name='detail'),

    path('agentt/', views.customers_list),
    path('agentt/<int:pk>/', views.customers_detail), 
    
]