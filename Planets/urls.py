# In your Django app's urls.py file
from django.urls import path
from . import views

urlpatterns = [
    # Define similar URL patterns for audio and video views
    path('search/', views.search, name='search'),
    path("",views.home,name='home'),
]
