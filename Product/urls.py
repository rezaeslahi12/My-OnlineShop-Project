from django.urls import path 
from .views import Product,productdetail,AddPost,Post_Like,Post_UnLike
urlpatterns = [
    path('',Product.as_view(),name='home'),
    path('product/<pk>',productdetail.as_view(),name='detail'),
    path('additem',AddPost,name='additem'),
    path('like/<id>',Post_Like, name= 'postlike'),
    path('unlike/<id>',Post_UnLike, name = 'postulike')
]