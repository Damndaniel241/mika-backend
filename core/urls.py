from django.urls import path
from .views import create_url,redirect_to_url

urlpatterns = [
    path('create-url/',create_url),
    path('<str:short_code>',redirect_to_url)
]