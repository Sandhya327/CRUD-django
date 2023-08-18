
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name="about"),
    path('insert',views.insertData,name="insertData"),
    path('delete/<id>',views.deleteData,name="deleteData"),
    path('update/<id>',views.updateData,name="updateData"),
]