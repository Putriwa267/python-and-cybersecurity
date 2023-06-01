from django.urls import path
from . import views


app_name = 'toko'

urlpatterns = [
    path('', views.HomeViews.as_view(), name='home'),
]