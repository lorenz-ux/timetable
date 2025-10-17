from django.urls import path
from . import views

urlpatterns = [
    path('',views.periode, name="periode")
]
