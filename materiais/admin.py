from django.contrib import admin
from .models import (
    Tile, TileCalculation,
    Plywood, PlywoodCalculation,
)


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'length', 'width', 'pieces_per_box', 'price_per_box', 'waste_percentage')
    search_fields = ('name',)


@admin.register(TileCalculation)
class TileCalculationAdmin(admin.ModelAdmin):
    list_display = ('tile', 'total_boxes', 'total_pieces', 'total_cost')
    list_filter = ('tile',)


@admin.register(Plywood)
class PlywoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'length', 'width', 'price_per_sheet', 'waste_percentage')
    search_fields = ('name',)


@admin.register(PlywoodCalculation)
class PlywoodCalculationAdmin(admin.ModelAdmin):
    list_display = ('plywood', 'total_sheets', 'total_cost')
    list_filter = ('plywood',)
