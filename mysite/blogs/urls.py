from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blogs_main'),
    path('<int:post_id>/', views.detail, name='blogs_detail'),
    path('add_post/', views.add_post, name='blogs_add_post'),
    path('save_post/<int:post_id>', views.save_post, name='blogs_save_post'),
]
