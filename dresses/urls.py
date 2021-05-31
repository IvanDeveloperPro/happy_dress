from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dress/<int:dress_id>/', views.single_dress, name='single_dress'),
    path('create/', views.create_dress, name='create_dress'),
    path('edit/<int:id_dress>/', views.edit_dress, name='edit_dress'),
    path('delete/<int:id_dress>/', views.delete_dress, name='delete_dress')
]
