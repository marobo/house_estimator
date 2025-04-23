from django import forms
from .models import (
    Room, Tile, TileCalculation,
    Plywood, PlywoodCalculation,
    ElectricComponent, ElectricalCalculation
)


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'length', 'width', 'quantity', 'room_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'length': forms.NumberInput(attrs={'class': 'form-control'}),
            'width': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_type': forms.Select(attrs={'class': 'form-control'}),
        }


class TileForm(forms.ModelForm):
    class Meta:
        model = Tile
        fields = [
            'name', 'length', 'width', 'pieces_per_box',
            'price_per_box', 'waste_percentage'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'length': forms.NumberInput(attrs={'class': 'form-control'}),
            'width': forms.NumberInput(attrs={'class': 'form-control'}),
            'pieces_per_box': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_per_box': forms.NumberInput(attrs={'class': 'form-control'}),
            'waste_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class TileCalculationForm(forms.ModelForm):
    class Meta:
        model = TileCalculation
        fields = [
            'room', 'tile', 'total_boxes', 'total_pieces',
            'total_cost', 'waste_percentage'
        ]
        widgets = {
            'room': forms.Select(attrs={'class': 'form-control'}),
            'tile': forms.Select(attrs={'class': 'form-control'}),
            'total_boxes': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}
            ),
            'total_pieces': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}
            ),
            'total_cost': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}
            ),
            'waste_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'room' in self.data and 'tile' in self.data:
            room = Room.objects.get(pk=self.data['room'])
            tile = Tile.objects.get(pk=self.data['tile'])
            result = tile.calculate_requirements(room)
            self.initial['total_boxes'] = result['total_boxes']
            self.initial['total_pieces'] = result['total_pieces']
            self.initial['total_cost'] = result['total_cost']
            self.initial['waste_percentage'] = tile.waste_percentage


class PlywoodForm(forms.ModelForm):
    class Meta:
        model = Plywood
        fields = ['name', 'length', 'width', 'price_per_sheet', 'waste_percentage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'length': forms.NumberInput(attrs={'class': 'form-control'}),
            'width': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_per_sheet': forms.NumberInput(attrs={'class': 'form-control'}),
            'waste_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PlywoodCalculationForm(forms.ModelForm):
    class Meta:
        model = PlywoodCalculation
        fields = ['room', 'plywood', 'total_sheets', 'total_cost', 'waste_percentage']
        widgets = {
            'room': forms.Select(attrs={'class': 'form-control'}),
            'plywood': forms.Select(attrs={'class': 'form-control'}),
            'total_sheets': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}
            ),
            'total_cost': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}
            ),
            'waste_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'room' in self.data and 'plywood' in self.data:
            room = Room.objects.get(pk=self.data['room'])
            plywood = Plywood.objects.get(pk=self.data['plywood'])
            result = plywood.calculate_requirements(room)
            self.initial['total_sheets'] = result['total_sheets']
            self.initial['total_cost'] = result['total_cost']
            self.initial['waste_percentage'] = plywood.waste_percentage


class ElectricComponentForm(forms.ModelForm):
    class Meta:
        model = ElectricComponent
        fields = ['name', 'unit_price', 'unit', 'component_type', 'default_quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'component_type': forms.Select(attrs={'class': 'form-control'}),
            'default_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ElectricalCalculationForm(forms.ModelForm):
    class Meta:
        model = ElectricalCalculation
        fields = ['room', 'component', 'quantity', 'total_cost']
        widgets = {
            'room': forms.Select(attrs={'class': 'form-control'}),
            'component': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}
            ),
            'total_cost': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'room' in self.data and 'component' in self.data:
            room = Room.objects.get(pk=self.data['room'])
            component = ElectricComponent.objects.get(pk=self.data['component'])
            result = component.calculate_requirements(room)
            self.initial['quantity'] = result['quantity']
            self.initial['total_cost'] = result['total_cost'] 