from django.contrib import admin
from .models import Product, Profile, Categoty
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','first_name')
    list_display = ('user','phone','email', 'first_name','phone')
    list_filter = [ 'country', 'first_name', ]
    search_fields = ['first_name','country','city' ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller','available')
    list_filter = [ 'pub_date','name' ]
    search_fields = ['category','name','seller' ]


admin.site.register(Profile,ProfileAdmin)
admin.site.register(Categoty)
admin.site.register(Product, ProductAdmin)