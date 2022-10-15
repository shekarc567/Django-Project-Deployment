from django.urls import path, re_path
from Courses import views

urlpatterns = [
    re_path(r'^Courses', views.index_1, name='index_1'),
]