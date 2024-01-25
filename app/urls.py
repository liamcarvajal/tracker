from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_app_items),
    path('insert_meal/', views.insert_meal_item, name='insert_meal_item'),
    path('delete_meal<int:meal_id>/', views.delete_meal_item, name='delete_meal_item')
]