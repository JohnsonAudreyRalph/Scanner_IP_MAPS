from django.urls import path
from .views import *

urlpatterns = [
    path('', Index),
    path('WEB_SERVER/', Read),
]