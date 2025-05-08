from django.contrib import admin
from .models import Tile, Plywood, ElectricComponent, Calculation


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    list_display = ('name', 'length', 'width', 'pieces_per_box', 'price_per_box')
    search_fields = ('name',)


@admin.register(Plywood)
class PlywoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'length', 'width', 'price_per_sheet')
    search_fields = ('name',)


@admin.register(ElectricComponent)
class ElectricComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_price', 'unit')
    search_fields = ('name',)


@admin.register(Calculation)
class CalculationAdmin(admin.ModelAdmin):
    list_display = (
        'category', 'material', 'room_length', 'room_width',
        'room_quantity', 'waste_percentage', 'total_cost', 'calculation_date'
    )
    list_filter = ('category', 'calculation_date')
    search_fields = ('category',)
