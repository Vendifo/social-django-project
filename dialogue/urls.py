from django.urls import path
from . import views

urlpatterns = [
    path('', views.dialogue, name='dialogue'),
    
]