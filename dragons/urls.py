from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dragons/<int:dragon_id>/feed/', views.feed_dragon, name='feed_dragon'),
]
