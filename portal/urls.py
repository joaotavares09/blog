from django.urls import path
from . import views

urlpatterns = [
	path('', views.area_list, name='area_list'),
	path('post/list', views.area_post_list, name='area_post_list'),
	
	path('post/<int:pk>/', views.area_detail, name='area_detail'),
	path('post/<int:pk>/', views.area_post_detail, name='area_post_detail'),
	
	path('post/new', views.area_new, name='area_new'),
	path('post/tipo', views.area_post_new, name='area_post_new'),
	
	path('post/<pk>/remove', views.area_remove, name='area_remove'),
	path('post/<pk>/removearea', views.area_post_remove, name='area_post_remove'),
	
	path('post/<int:pk>/publicar/', views.area_publicar, name='area_publicar'),
	
	path('post/<int:pk>/edit/', views.area_edit, name='area_edit'),
	path('post/<int:pk>/editarea/', views.area_post_edit, name='area_post_edit'),
]