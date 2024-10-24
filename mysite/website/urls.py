from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.landing_page, name='index'),
    path('retos/', views.retos, name='retos'),
    path('huella/', views.calcula_huella, name='huella'),
    path('calcular-huella/', views.calcular_huella, name='calcular_huella'),
]
