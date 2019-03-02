from django.urls import path
from . import views

#from .views import (BlogDetailView)
# SET THE NAMESPACE!
app_name = 'book'

urlpatterns = [

    # path('detail/', views.detail, name='index'),
    # path('register/',views.register,name='register'),
    # path('user_login/',views.user_login,name='user_login'),
    # path('logout/', views.user_logout, name='logout'),
    # path('special/',views.special,name='special'),
    path('rahul/new/book/', views.BlogCreateView.as_view(), name='new_book'),
    # path('rahul/', views.newbook, name='book'),
    path('rahul/new/cat/', views. CatCreateView.as_view(), name='new_cat'),
    path('rahul/new/product/', views.BlogListView, name='product'),
    path('rahul/new/product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]
