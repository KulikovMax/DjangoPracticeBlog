from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blogs_main'),
    path('<int:post_id>/', views.detail, name='blogs_detail')
]
