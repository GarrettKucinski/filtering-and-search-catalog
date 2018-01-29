from django.urls import path
from . import views

app_name = 'minerals'

urlpatterns = [
    path('<int:pk>', views.mineral_detail, name='mineral_detail'),
]
