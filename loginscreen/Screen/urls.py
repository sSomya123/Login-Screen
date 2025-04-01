from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL of the app, mapping to the index view
]
