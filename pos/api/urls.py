from django.urls import path, include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    TableRestoListApiView, TableRestoDetailApiView,
)
app_name='api'

urlpatterns = [
    #path('api/vl/login', LoginView.as_view()),
    #path('api/vl/logiout', LogoutView.as_view()),
    #path('api/vl/register', RegisterWaitressApi.as_view()),
    path('api/table_resto', views.TableRestoListApiView.as_view()),
    path('api/table_resto/<int:id>', views.TableRestoDetailApiView.as_view()),
]