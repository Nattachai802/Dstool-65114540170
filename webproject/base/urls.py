from django.contrib import admin
from django.urls import path , include
from base.views import *
urlpatterns = [
    path('',course_list,name='list'),
    path('update/<str:pk>',updateview.as_view(),name='update')
]
