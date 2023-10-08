from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
     path("accounts/profile/",views.index),
]
