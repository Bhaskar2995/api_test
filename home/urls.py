from django.contrib import admin
from django.urls import path

from .views import StudentView

urlpatterns = [
    path('student/<int:id>', StudentView.as_view(), name='student'),
    path('student', StudentView.as_view(), name='student'),

]
