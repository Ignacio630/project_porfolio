from django.urls import path
from .views import * 

urlpatterns = [
    path('contact/', contact_form, name='contact_form'),
]