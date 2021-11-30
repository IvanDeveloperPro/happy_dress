from django.urls import path

from . import views

urlpatterns = [
    path('', views.DressListView.as_view(), name='index'),
    path('dress/<int:pk>/', views.DressDetailView.as_view(), name='single_dress'),
    path('create/', views.create_dress, name='create_dress'),
    path('basket/', views.basket_dress, name='basket'),
    path('order/<int:basket_id>/', views.order, name='order'),
    path('basket-add/<int:id_dress>/', views.add_dress_basket, name='add_basket'),
    path('basket-del/<int:id_dress>/', views.delete_dress_basket, name='del_basket'),
    path('basket/add/', views.basket_add, name='basket_add_api'),
    path('basket/del/', views.basket_del, name='basket_del_api'),
    path('edit/<int:id_dress>/', views.edit_dress, name='edit_dress'),
    path('delete/<int:id_dress>/', views.delete_dress, name='delete_dress')
]
