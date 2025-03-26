from django.urls import path
from . import views

urlpatterns = [
    path('', views.college_list, name='college_list'),
    path('create', views.college_create, name='college_create'),
    path('<int:pk>/', views.college_detail, name='college_detail'),
    path('<int:pk>/edit/', views.college_update, name='college_update'),
    path('<int:pk>/delete/', views.college_delete, name='college_delete'),
]