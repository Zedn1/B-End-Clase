from django.urls import path
from cuchufli import views

urlpatterns = [
    path('pagina1/', views.pag1),
    path('pagina2/', views.pag2),
]
