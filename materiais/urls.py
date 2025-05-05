from django.urls import path
from . import views

app_name = 'materiais'

urlpatterns = [
    path('', views.home, name='home'),

    # Tile URLs
    path('tiles/', views.TileListView.as_view(), name='tile_list'),
    path('tiles/create/', views.TileCreateView.as_view(), name='tile_create'),
    path('tiles/<int:pk>/edit/', views.TileUpdateView.as_view(), name='tile_edit'),
    path('tiles/<int:pk>/delete/', views.TileDeleteView.as_view(), name='tile_delete'),
    path('tile-calculations/', views.TileCalculationListView.as_view(), name='tile_calculation_list'),
    path('tile-calculations/create/', views.TileCalculationCreateView.as_view(), name='tile_calculation_create'),
    path('tile-calculations/<int:pk>/edit/', views.TileCalculationUpdateView.as_view(), name='tile_calculation_edit'),
    path('tile-calculations/<int:pk>/delete/', views.TileCalculationDeleteView.as_view(), name='tile_calculation_delete'),

    # Plywood URLs
    path('plywoods/', views.PlywoodListView.as_view(), name='plywood_list'),
    path('plywoods/create/', views.PlywoodCreateView.as_view(), name='plywood_create'),
    path('plywoods/<int:pk>/edit/', views.PlywoodUpdateView.as_view(), name='plywood_edit'),
    path('plywoods/<int:pk>/delete/', views.PlywoodDeleteView.as_view(), name='plywood_delete'),
    path('plywood-calculations/', views.PlywoodCalculationListView.as_view(), name='plywood_calculation_list'),
    path('plywood-calculations/create/', views.PlywoodCalculationCreateView.as_view(), name='plywood_calculation_create'),
    path('plywood-calculations/<int:pk>/edit/', views.PlywoodCalculationUpdateView.as_view(), name='plywood_calculation_edit'),
    path('plywood-calculations/<int:pk>/delete/', views.PlywoodCalculationDeleteView.as_view(), name='plywood_calculation_delete'),

    # Electrical URLs
    path('electric-components/', views.ElectricComponentListView.as_view(), name='electric_component_list'),
    path('electric-components/create/', views.ElectricComponentCreateView.as_view(), name='electric_component_create'),
    path('electrical-calculations/', views.ElectricalCalculationListView.as_view(), name='electrical_calculation_list'),
    path('electrical-calculations/create/', views.ElectricalCalculationCreateView.as_view(), name='electrical_calculation_create'),
]
