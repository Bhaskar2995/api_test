from django.contrib import admin
from django.urls import path

from .views import Student

urlpatterns = [
    path('student/<int:id>', Student.as_view(), name='student'),
    path('student/', Student.as_view(), name='student'),

]
