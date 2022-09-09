from dataclasses import field
from msilib.schema import Class
from django.contrib import admin
from .models import product
class BlogAdmin(admin.ModelAdmin):
    fieldsets =[
        (None,                              {'fields':['P_name']}),
        ('Discrption Information',          {'fields':['discrption','author','price',]}),
        ('images',                           {'fields':['image']}),
        ('likes',                           {'fields':['like']}),
        
    ]
    list_display =[
        'P_name','date','price'
    ]
    search_fields =[
        'P_name','date','price','author'
    ]
admin.site.register(product,BlogAdmin)
