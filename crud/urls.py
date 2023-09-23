from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    path('', home),
    path('student/',post_student),
    path('students/update/<int:id>/', update_student, name='update-student'),
    path ('students/delete/', delete_student, name='delete-student'),

]
