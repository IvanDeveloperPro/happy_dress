from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dress/<int:dress_id>/', views.single_dress, name='single_dress'),
    path('create/', views.create_edit_dress, name='create_dress')
]
