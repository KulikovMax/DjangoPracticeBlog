from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='polls_main'),
    path('<int:question_id>/', views.detail, name='polls_detail'),
    path('<int:question_id>/results', views.results, name='polls_results'),
    path('<int:question_id>/vote', views.vote, name='polls_vote'),
]
