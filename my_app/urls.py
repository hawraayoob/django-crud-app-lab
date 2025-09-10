from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Animal CRUD
    path('animals/', views.animal_index, name='animal_index'),
    path('animals/<int:pk>/', views.animal_detail, name='animal_detail'),
    path('animals/create/', views.animal_create, name='animal_create'),
    path('animals/<int:pk>/update/', views.animal_update, name='animal_update'),
    path('animals/<int:pk>/delete/', views.animal_delete, name='animal_delete'),

    # Toy CRUD
    path('toys/', views.toy_index, name='toy_index'),
    path('toys/<int:pk>/', views.toy_detail, name='toy_detail'),
    path('toys/create/', views.toy_create, name='toy_create'),
    path('toys/<int:pk>/update/', views.toy_update, name='toy_update'),
    path('toys/<int:pk>/delete/', views.toy_delete, name='toy_delete'),

    # Habitat CRUD
    path('habitats/', views.habitat_index, name='habitat_index'),
    path('habitats/<int:pk>/', views.habitat_detail, name='habitat_detail'),
    path('habitats/create/', views.habitat_create, name='habitat_create'),
    path('habitats/<int:pk>/update/', views.habitat_update, name='habitat_update'),
    path('habitats/<int:pk>/delete/', views.habitat_delete, name='habitat_delete'),

    # Signup
    path('signup/', views.signup, name='signup'),
]