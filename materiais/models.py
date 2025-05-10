from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import math
from django.contrib.auth.models import User


class Tile(models.Model):
    TILE_TYPE_CHOICES = [
        ('tile', 'Tile'),
        ('pvc', 'PVC'),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TILE_TYPE_CHOICES, default='tile')
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
        return (self.length * self.width) / 10000  # Convert to square meters (1 m2=(100 cm)×(100 cm)=10,000 cm2)

    def calculate_requirements(self, room_length, room_width, room_quantity=1, waste_percentage=None):
        room_area = room_length * room_width * room_quantity
        tile_area = self.area_per_piece
        waste_percentage = waste_percentage if waste_percentage is not None else self.waste_percentage
        total_pieces = math.ceil(room_area / tile_area * (1 + waste_percentage / 100))  # math.ceil() rounds up to the nearest integer
        total_boxes = math.ceil(total_pieces / self.pieces_per_box)  # math.ceil() rounds up to the nearest integer
        total_cost = total_boxes * self.price_per_box
        return {
            'total_pieces': total_pieces,
            'total_boxes': total_boxes,
            'total_cost': total_cost
        }


class TileCalculation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    def area_per_sheet(self):
        return self.length * self.width  # Area in square meters

    def calculate_requirements(self, room_length, room_width, room_quantity=1, waste_percentage=None):
        room_area = room_length * room_width * room_quantity
        plywood_area = self.area_per_sheet
        waste_percentage = waste_percentage if waste_percentage is not None else self.waste_percentage
        total_sheets = math.ceil(room_area / plywood_area * (1 + waste_percentage / 100))
        total_cost = total_sheets * self.price_per_sheet
        return {
            'total_sheets': total_sheets,
            'total_cost': total_cost
        }


class PlywoodCalculation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plywood = models.ForeignKey(Plywood, on_delete=models.CASCADE)
    room_length = models.FloatField(help_text="Room length in meters")
    room_width = models.FloatField(help_text="Room width in meters")
    room_quantity = models.IntegerField(default=1)
    total_sheets = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    waste_percentage = models.FloatField(
        help_text="Waste percentage for cutting and breakage (0-100%)",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    calculation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Plywood Calculation for {self.plywood.name} ({self.room_length}x{self.room_width}m)"
