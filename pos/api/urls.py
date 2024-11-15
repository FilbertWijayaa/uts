from django.urls import path
from api import views
from .views import (
    RegisterUserAPIView, LoginView
)
app_name='api'

urlpatterns = [
    path('api/register', RegisterUserAPIView.as_view()),
    path('api/login', LoginView.as_view()),
    path('api/menu_resto', views.MenuRestoView.as_view()),
    path('api/menu-resto-filter', views.MenuRestoFilterApi.as_view())
]