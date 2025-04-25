from django.urls import path
from . import views  # import views from the current app

urlpatterns = [
    path('backend/', views.show_name, name='show_name'),
]
