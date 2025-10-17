from django.urls import path
from . import views

urlpatterns = [
    path('', views.enseignant, name="enseignant")
]
