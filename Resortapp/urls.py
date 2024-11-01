from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('userProfile/', UserProfileView.as_view(), name='profile'),
    path('userProfile/update/<str:pk>/', UserProfileUpdateView.as_view(), name='profileUpdate'),
]