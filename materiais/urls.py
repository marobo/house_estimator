from django.urls import path
from . import views

app_name = 'materiais'

urlpatterns = [
    path('', views.home, name='home'),
    
    # Room URLs
    path('rooms/', views.RoomListView.as_view(), name='room_list'),
    path('rooms/create/', views.RoomCreateView.as_view(), name='room_create'),
    
    # Tile URLs
    path('tiles/', views.TileListView.as_view(), name='tile_list'),
    path('tiles/create/', views.TileCreateView.as_view(), name='tile_create'),
    path('tile-calculations/create/', 
         views.TileCalculationCreateView.as_view(), 
         name='tile_calculation_create'),
    
    # Plywood URLs
    path('plywoods/', views.PlywoodListView.as_view(), name='plywood_list'),
    path('plywoods/create/', views.PlywoodCreateView.as_view(), name='plywood_create'),
    path('plywood-calculations/create/', 
         views.PlywoodCalculationCreateView.as_view(), 
         name='plywood_calculation_create'),
    
    # Electrical URLs
    path('electric-components/', 
         views.ElectricComponentListView.as_view(), 
         name='electric_component_list'),
    path('electric-components/create/', 
         views.ElectricComponentCreateView.as_view(), 
         name='electric_component_create'),
    path('electrical-calculations/create/', 
         views.ElectricalCalculationCreateView.as_view(), 
         name='electrical_calculation_create'),
] 