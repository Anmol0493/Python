from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('members/', views.members),
    path('members/details/<int:id>', views.details)
]