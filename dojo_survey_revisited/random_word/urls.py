from django.urls import path
from . import views

urlpatterns = [
    path('', views.word),
    path('random_word', views.word),
    path('reset', views.reset),
]