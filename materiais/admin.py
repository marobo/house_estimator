from django.contrib import admin
from .models import (
    Tile, TileCalculation,
    Plywood, PlywoodCalculation,
    ElectricComponent, ElectricalCalculation
)


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    list_display = ('name', 'length', 'width', 'pieces_per_box', 'price_per_box')
    search_fields = ('name',)

@admin.register(TileCalculation)
class TileCalculationAdmin(admin.ModelAdmin):
    list_display = ('tile', 'total_boxes', 'total_pieces', 'total_cost')
    list_filter = ('tile',)

@admin.register(Plywood)
class PlywoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'length', 'width', 'price_per_sheet')
    search_fields = ('name',)

@admin.register(PlywoodCalculation)
class PlywoodCalculationAdmin(admin.ModelAdmin):
    list_display = ('plywood', 'total_sheets', 'total_cost')
    list_filter = ('plywood',)

@admin.register(ElectricComponent)
class ElectricComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_price', 'unit')
    search_fields = ('name',)

@admin.register(ElectricalCalculation)
class ElectricalCalculationAdmin(admin.ModelAdmin):
    list_display = ('component', 'quantity', 'total_cost')
    list_filter = ('component',)