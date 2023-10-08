
from django.urls import path
from . import views

urlpatterns = [
    path('deneme/', views.DenemeView.as_view(), name='deneme'),
    # Diğer URL'ler
]

