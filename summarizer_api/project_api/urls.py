from django.urls import path
from .views import SummarizerAPI

urlpatterns = [
   path('', SummarizerAPI.as_view(), name="api_views"),
]