from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import math


class Tile(models.Model):
    name = models.CharField(max_length=100)
    length = models.FloatField(help_text="Length in centimeters", validators=[MinValueValidator(0)])
    width = models.FloatField(help_text="Width in centimeters", validators=[MinValueValidator(0)])
    pieces_per_box = models.IntegerField(validators=[MinValueValidator(1)])
    price_per_box = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    waste_percentage = models.FloatField(
        default=10,
        help_text="Waste percentage for cutting and breakage (0-100%)",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return f"{self.name} ({self.length}x{self.width}cm)"

    @property
    def area_per_piece(self):
        return (self.length * self.width) / 10000  # Convert to square meters

    def calculate_requirements(self, room_length, room_width, room_quantity=1, waste_percentage=None):
        room_area = room_length * room_width * room_quantity
        tile_area = self.area_per_piece
        waste_percentage = waste_percentage if waste_percentage is not None else self.waste_percentage
        total_pieces = math.ceil(room_area / tile_area * (1 + waste_percentage / 100))
        total_boxes = math.ceil(total_pieces / self.pieces_per_box)
        total_cost = total_boxes * self.price_per_box
        return {
            'total_pieces': total_pieces,
            'total_boxes': total_boxes,
            'total_cost': total_cost
        }


class TileCalculation(models.Model):
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)
    room_length = models.FloatField(help_text="Room length in meters")
    room_width = models.FloatField(help_text="Room width in meters")
    room_quantity = models.IntegerField(default=1)
    total_boxes = models.FloatField()
    total_pieces = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    waste_percentage = models.FloatField(
        help_text="Waste percentage for cutting and breakage (0-100%)",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    calculation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tile.name} - {self.room_length}x{self.room_width}m - {self.calculation_date}"


class Plywood(models.Model):
    name = models.CharField(max_length=100)
    length = models.FloatField(help_text="Length in meters", validators=[MinValueValidator(0)])
    width = models.FloatField(help_text="Width in meters", validators=[MinValueValidator(0)])
    price_per_sheet = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    waste_percentage = models.FloatField(default=5, help_text="Waste percentage for cutting")

    def __str__(self):
        return f"{self.name} ({self.length}x{self.width}m)"

    @property
    def area(self):
        return self.length * self.width

    def calculate_requirements(self, room_length, room_width, room_quantity=1):
        room_area = room_length * room_width * room_quantity
        plywood_area = self.area
        total_sheets = math.ceil(room_area / plywood_area * (1 + self.waste_percentage / 100))
        total_cost = total_sheets * self.price_per_sheet
        return {
            'total_sheets': total_sheets,
            'total_cost': total_cost
        }


class PlywoodCalculation(models.Model):
    plywood = models.ForeignKey(Plywood, on_delete=models.CASCADE)
    room_length = models.FloatField(help_text="Room length in meters")
    room_width = models.FloatField(help_text="Room width in meters")
    room_quantity = models.IntegerField(default=1)
    total_sheets = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    waste_percentage = models.FloatField()
    calculation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Plywood Calculation for {self.plywood.name} ({self.room_length}x{self.room_width}m)"


class ElectricComponent(models.Model):
    name = models.CharField(max_length=200)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=50)
    component_type = models.CharField(max_length=50, choices=[
        ('cable', 'Cable'),
        ('switch', 'Switch'),
        ('socket', 'Socket'),
        ('light', 'Light'),
        ('other', 'Other'),
    ])
    default_quantity = models.IntegerField(default=1, help_text="Default quantity per room")

    def __str__(self):
        return self.name

    def calculate_requirements(self, room_length, room_width, room_quantity=1):
        if self.component_type == 'cable':
            # Cable calculation based on room dimensions and wiring paths
            perimeter = 2 * (room_length + room_width) * room_quantity
            return {
                'quantity': perimeter,
                'total_cost': perimeter * self.unit_price
            }
        else:
            # For other components, use default quantity
            quantity = self.default_quantity * room_quantity
            return {
                'quantity': quantity,
                'total_cost': quantity * self.unit_price
            }


class ElectricalCalculation(models.Model):
    component = models.ForeignKey(ElectricComponent, on_delete=models.CASCADE)
    room_length = models.FloatField(help_text="Room length in meters")
    room_width = models.FloatField(help_text="Room width in meters")
    room_quantity = models.IntegerField(default=1)
    quantity = models.FloatField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    calculation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Electrical Calculation for {self.component.name} ({self.room_length}x{self.room_width}m)"
