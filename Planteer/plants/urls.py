
from django.urls import path
from . import views

app_name = "plants"

urlpatterns = [
    path('all/', views.all_plants_view, name='all_plants'),

    path('<int:id>/detail/', views.plant_detail_view, name='plant_detail'),

    path('new/', views.create_plant_view, name='create_plant'),

    path('<int:id>/update/', views.update_plant_view, name='update_plant'),

    path('<int:id>/delete/', views.delete_plant_view, name='delete_plant'),
    
    path('search/', views.search_view, name='search'),
]