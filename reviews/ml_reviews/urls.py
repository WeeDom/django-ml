from django.urls import path

from . import views

urlpatterns = [
    # path('reviews', views.index, name='index'),
    path('/', views.home, name='home'),
    path('', views.home, name='home'),
    path('<int:review_id>/', views.detail, name='detail'),
    path('<int:review_id>/review/', views.review, name='review'),
    path('<int:opinion_id>/opinion/', views.opinion, name='opinion'),
    ]
