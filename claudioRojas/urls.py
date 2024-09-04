from django.urls import path
from claudioRojas import views

urlpatterns = [
    path('indexZed/', views.indexZed),
    path('Zed/', views.Zed),
]