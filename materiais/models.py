from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
import math

class Room(models.Model):
    name = models.CharField(max_length=100)
    length = models.FloatField(help_text="Length in meters", validators=[MinValueValidator(0)])
    width = models.FloatField(help_text="Width in meters", validators=[MinValueValidator(0)])
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    room_type = models.CharField(max_length=50, choices=[
        ('bedroom', 'Bedroom'),
        ('living_room', 'Living Room'),
        ('kitchen', 'Kitchen'),
        ('bathroom', 'Bathroom'),
        ('balcony', 'Balcony'),
    ])

    def __str__(self):
        return f"{self.name} ({self.length}x{self.width}m)"

    @property
    def area(self):
        return self.length * self.width * self.quantity

    @property
    def perimeter(self):
        return 2 * (self.length + self.width) * self.quantity

class Tile(models.Model):
    name = models.CharField(max_length=100)
    length = models.FloatField(help_text="Length in centimeters", validators=[MinValueValidator(0)])
    width = models.FloatField(help_text="Width in centimeters", validators=[MinValueValidator(0)])
    pieces_per_box = models.IntegerField(validators=[MinValueValidator(1)])
    price_per_box = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    waste_percentage = models.FloatField(default=10, help_text="Waste percentage for cutting and breakage")

    def __str__(self):
        return f"{self.name} ({self.length}x{self.width}cm)"

    @property
    def area_per_piece(self):
        return (self.length * self.width) / 10000  # Convert to square meters

    def calculate_requirements(self, room):
        room_area = room.area
        tile_area = self.area_per_piece
        total_pieces = math.ceil(room_area / tile_area * (1 + self.waste_percentage / 100))
        total_boxes = math.ceil(total_pieces / self.pieces_per_box)
        total_cost = total_boxes * self.price_per_box
        return {
            'total_pieces': total_pieces,
            'total_boxes': total_boxes,
            'total_cost': total_cost
        }

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

    def calculate_requirements(self, room):
        room_area = room.area
        plywood_area = self.area
        total_sheets = math.ceil(room_area / plywood_area * (1 + self.waste_percentage / 100))
        total_cost = total_sheets * self.price_per_sheet
        return {
            'total_sheets': total_sheets,
            'total_cost': total_cost
        }

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

    def calculate_requirements(self, room):
        if self.component_type == 'cable':
            # Cable calculation based on room dimensions and wiring paths
            if room.room_type == 'bedroom':
                switch_to_ceiling = 2  # meters
                ceiling_to_light = 1.5  # meters
                total_length = (switch_to_ceiling + ceiling_to_light) * room.quantity
            elif room.room_type == 'living_room':
                switch_to_ceiling = 2.5  # meters
                ceiling_to_light = 2  # meters
                total_length = (switch_to_ceiling + ceiling_to_light) * room.quantity
            else:
                total_length = room.perimeter * 0.5  # Default estimation
            return {
                'quantity': total_length,
                'total_cost': total_length * self.unit_price
            }
        else:
            # For other components, use default quantity
            quantity = self.default_quantity * room.quantity
            return {
                'quantity': quantity,
                'total_cost': quantity * self.unit_price
            }

class TileCalculation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)
    total_boxes = models.FloatField()
    total_pieces = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    waste_percentage = models.FloatField()
    calculation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room} - {self.tile}"

class PlywoodCalculation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    plywood = models.ForeignKey(Plywood, on_delete=models.CASCADE)
    total_sheets = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    waste_percentage = models.FloatField()
    calculation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room} - {self.plywood}"

class ElectricalCalculation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    component = models.ForeignKey(ElectricComponent, on_delete=models.CASCADE)
    quantity = models.FloatField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    calculation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room} - {self.component}" 