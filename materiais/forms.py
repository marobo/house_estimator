from django import forms
from .models import (
    Tile, 
    Plywood, 
    ElectricComponent, 
    Calculation
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


class CalculationForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=Calculation._meta.get_field('category').choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    material = forms.ModelChoiceField(
        queryset=Tile.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Calculation
        fields = [
            'category',
            'material',
            'room_length',
            'room_width',
            'room_quantity',
            'waste_percentage',
            'total_cost',
        ]
        widgets = {
            'room_length': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'room_width': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'room_quantity': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'waste_percentage': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'total_cost': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.data:
            category = self.data.get('category')
            if category == 'tile':
                self.fields['material'].queryset = Tile.objects.all()
            elif category == 'plywood':
                self.fields['material'].queryset = Plywood.objects.all()
            elif category == 'electrical':
                self.fields['material'].queryset = ElectricComponent.objects.all()
        elif self.instance.pk:
            ct = self.instance.content_type
            if ct.model == 'tile':
                self.fields['material'].queryset = Tile.objects.all()
            elif ct.model == 'plywood':
                self.fields['material'].queryset = Plywood.objects.all()
            elif ct.model == 'electriccomponent':
                self.fields['material'].queryset = ElectricComponent.objects.all()
