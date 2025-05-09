from django import forms
from .models import (
    Tile, TileCalculation,
    Plywood, PlywoodCalculation,
)


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
            'tile', 'room_length', 'room_width', 'room_quantity',
            'waste_percentage'
        ]
        widgets = {
            'tile': forms.Select(attrs={'class': 'form-control'}),
            'room_length': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_width': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'waste_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize waste percentage with tile's default value if creating new calculation
        if not self.instance.pk and 'tile' in self.initial:
            tile = self.initial['tile']
            if isinstance(tile, Tile):
                self.initial['waste_percentage'] = tile.waste_percentage

    def clean(self):
        cleaned_data = super().clean()
        tile = cleaned_data.get('tile')
        room_length = cleaned_data.get('room_length')
        room_width = cleaned_data.get('room_width')
        room_quantity = cleaned_data.get('room_quantity', 1)
        waste_percentage = cleaned_data.get('waste_percentage')

        if tile and room_length and room_width:
            try:
                result = tile.calculate_requirements(
                    room_length, room_width, room_quantity, waste_percentage
                )
                # Set the calculated values on the instance
                self.instance.total_boxes = result['total_boxes']
                self.instance.total_pieces = result['total_pieces']
                self.instance.total_cost = result['total_cost']
            except (ValueError, TypeError) as e:
                raise forms.ValidationError(
                    "Error calculating requirements: " + str(e)
                )
        else:
            if not tile:
                self.add_error('tile', 'This field is required.')
            if not room_length:
                self.add_error('room_length', 'This field is required.')
            if not room_width:
                self.add_error('room_width', 'This field is required.')

        return cleaned_data


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
        fields = [
            'plywood', 'room_length', 'room_width', 'room_quantity',
            'waste_percentage'
        ]
        widgets = {
            'plywood': forms.Select(attrs={'class': 'form-control'}),
            'room_length': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_width': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'waste_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize waste percentage with plywood's default value if creating new calculation
        if not self.instance.pk and 'plywood' in self.initial:
            plywood = self.initial['plywood']
            if isinstance(plywood, Plywood):
                self.initial['waste_percentage'] = plywood.waste_percentage

    def clean(self):
        cleaned_data = super().clean()
        plywood = cleaned_data.get('plywood')
        room_length = cleaned_data.get('room_length')
        room_width = cleaned_data.get('room_width')
        room_quantity = cleaned_data.get('room_quantity', 1)
        waste_percentage = cleaned_data.get('waste_percentage')

        if plywood and room_length and room_width:
            try:
                result = plywood.calculate_requirements(
                    room_length, room_width, room_quantity, waste_percentage
                )
                # Set the calculated values on the instance
                self.instance.total_sheets = result['total_sheets']
                self.instance.total_cost = result['total_cost']
            except (ValueError, TypeError) as e:
                raise forms.ValidationError(
                    "Error calculating requirements: " + str(e)
                )
        else:
            if not plywood:
                self.add_error('plywood', 'This field is required.')
            if not room_length:
                self.add_error('room_length', 'This field is required.')
            if not room_width:
                self.add_error('room_width', 'This field is required.')

        return cleaned_data
