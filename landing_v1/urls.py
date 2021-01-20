from django.urls import path
from . import views

app_name = 'landing_v1'
urlpatterns = [
    path('', views.index, name='home'),
]
