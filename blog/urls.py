from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup),
    path('loginn/', views.loginn),
    path('home/', views.home),
    path('newpost/', views.newPost, name='new-post'),
    path('mypost/', views.myPost, name='my-post'),
    path('signout/', views.signout, name='signout-btn'),
]