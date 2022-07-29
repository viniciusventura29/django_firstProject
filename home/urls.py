from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_index, name='homeindex'),
    path('details/<int:id>', views.home_details, name='details'),
    path('save_user/', views.save_user, name='save_user'),
]
