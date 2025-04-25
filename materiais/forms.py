from django import forms
from .models import (
    Tile, TileCalculation,
    Plywood, PlywoodCalculation,
    ElectricComponent, ElectricalCalculation
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
            'total_boxes', 'total_pieces', 'total_cost', 'waste_percentage'
        ]
        widgets = {
            'tile': forms.Select(attrs={'class': 'form-control'}),
            'room_length': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_width': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_boxes': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}
            ),
            'total_pieces': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}
            ),
            'total_cost': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}
            ),
            'waste_percentage': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        tile = cleaned_data.get('tile')
        room_length = cleaned_data.get('room_length')
        room_width = cleaned_data.get('room_width')
        room_quantity = cleaned_data.get('room_quantity', 1)

        if tile and room_length and room_width:
            try:
                result = tile.calculate_requirements(
                    room_length, room_width, room_quantity
                )
                cleaned_data['total_boxes'] = result['total_boxes']
                cleaned_data['total_pieces'] = result['total_pieces']
                cleaned_data['total_cost'] = result['total_cost']
                cleaned_data['waste_percentage'] = tile.waste_percentage
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['total_boxes'].required = False
        self.fields['total_pieces'].required = False
        self.fields['total_cost'].required = False
        self.fields['waste_percentage'].required = False

        if (self.is_bound and 'tile' in self.data and 
            'room_length' in self.data and 'room_width' in self.data):
            try:
                tile = Tile.objects.get(pk=self.data['tile'])
                room_length = float(self.data['room_length'])
                room_width = float(self.data['room_width'])
                room_quantity = int(self.data.get('room_quantity', 1))

                result = tile.calculate_requirements(
                    room_length, room_width, room_quantity
                )

                self.initial['total_boxes'] = result['total_boxes']
                self.initial['total_pieces'] = result['total_pieces']
                self.initial['total_cost'] = result['total_cost']
                self.initial['waste_percentage'] = tile.waste_percentage
            except (ValueError, Tile.DoesNotExist):
                pass


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
            'total_sheets', 'total_cost', 'waste_percentage'
        ]
        widgets = {
            'plywood': forms.Select(attrs={'class': 'form-control'}),
            'room_length': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_width': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
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
        if 'plywood' in self.data and 'room_length' in self.data and 'room_width' in self.data:
            plywood = Plywood.objects.get(pk=self.data['plywood'])
            room_length = float(self.data['room_length'])
            room_width = float(self.data['room_width'])
            room_quantity = int(self.data.get('room_quantity', 1))
            result = plywood.calculate_requirements(room_length, room_width, room_quantity)
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
        fields = [
            'component', 'room_length', 'room_width', 'room_quantity',
            'quantity', 'total_cost'
        ]
        widgets = {
            'component': forms.Select(attrs={'class': 'form-control'}),
            'room_length': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_width': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}
            ),
            'total_cost': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'component' in self.data and 'room_length' in self.data and 'room_width' in self.data:
            component = ElectricComponent.objects.get(pk=self.data['component'])
            room_length = float(self.data['room_length'])
            room_width = float(self.data['room_width'])
            room_quantity = int(self.data.get('room_quantity', 1))
            result = component.calculate_requirements(room_length, room_width, room_quantity)
            self.initial['quantity'] = result['quantity']
            self.initial['total_cost'] = result['total_cost']
