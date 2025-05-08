from django.contrib import admin
from .models import Tile, Plywood, ElectricComponent, Calculation

admin.site.register(Tile)
admin.site.register(Plywood)
admin.site.register(ElectricComponent)

@admin.register(Calculation)
class CalculationAdmin(admin.ModelAdmin):
    list_display = (
        'category', 'material', 'room_length', 'room_width',
        'room_quantity', 'waste_percentage', 'total_cost', 'calculation_date'
    )
    list_filter = ('category', 'calculation_date')
    search_fields = ('category',)
