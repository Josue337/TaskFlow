from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # US15: Dashboard principal
    path('', views.dashboard_home, name='home'),
    
    # US18, US19: Estadísticas
    path('statistics/', views.statistics_view, name='statistics'),
]
