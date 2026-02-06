from django.urls import path
from . import views

urlpatterns = [
    path('', views.voter_list, name='voter_list'),
    path('new/', views.voter_create, name='voter_create'),
    path('<int:pk>/edit/', views.voter_update, name='voter_update'),
    path('<int:pk>/delete/', views.voter_delete, name='voter_delete'),
    path('<int:pk>/', views.voter_detail, name='voter_detail'),
    path('search/', views.voter_search, name='voter_search'),
]
