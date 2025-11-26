from django.urls import path
from . import views

urlpatterns = [
    path('query/', views.query_analysis, name='query_analysis'),
    path('areas/', views.get_available_areas, name='get_available_areas'),
    path('health/', views.health_check, name='health_check'),
]
