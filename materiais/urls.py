from django.urls import path
from . import views

app_name = 'materiais'

urlpatterns = [
    path('', views.home, name='home'),

    # Tile URLs
    path('tiles/', views.TileListView.as_view(), name='tile_list'),
    path('tiles/create/', views.TileCreateView.as_view(), name='tile_create'),
    path('tiles/<int:pk>/', views.TileDetailView.as_view(), name='tile_detail'),
    path('tiles/<int:pk>/edit/', views.TileUpdateView.as_view(), name='tile_edit'),
    path('tiles/<int:pk>/delete/', views.TileDeleteView.as_view(), name='tile_delete'),

    # Plywood URLs
    path('plywoods/', views.PlywoodListView.as_view(), name='plywood_list'),
    path('plywoods/create/', views.PlywoodCreateView.as_view(), name='plywood_create'),
    path('plywoods/<int:pk>/', views.PlywoodDetailView.as_view(), name='plywood_detail'),
    path('plywoods/<int:pk>/edit/', views.PlywoodUpdateView.as_view(), name='plywood_edit'),
    path('plywoods/<int:pk>/delete/', views.PlywoodDeleteView.as_view(), name='plywood_delete'),

    # Electrical URLs
    path('electric-components/', views.ElectricComponentListView.as_view(), name='electric_component_list'),
    path('electric-components/create/', views.ElectricComponentCreateView.as_view(), name='electric_component_create'),
    path('electric-components/<int:pk>/', views.ElectricComponentDetailView.as_view(), name='electric_component_detail'),
    path('electric-components/<int:pk>/edit/', views.ElectricComponentUpdateView.as_view(), name='electric_component_edit'),
    path('electric-components/<int:pk>/delete/', views.ElectricComponentDeleteView.as_view(), name='electric_component_delete'),

    # Calculation URLs
    path('calculations/', views.CalculationListView.as_view(), name='calculation_list'),
    path('calculations/create/', views.CalculationCreateView.as_view(), name='calculation_create'),
    path('calculations/<int:pk>/', views.CalculationDetailView.as_view(), name='calculation_detail'),
    path('calculations/<int:pk>/edit/', views.CalculationUpdateView.as_view(), name='calculation_update'),
    path('calculations/<int:pk>/delete/', views.CalculationDeleteView.as_view(), name='calculation_delete'),
    # AJAX endpoint for dynamic material selection
    path('ajax/get-materials/', views.get_materials, name='get_materials'),
]
