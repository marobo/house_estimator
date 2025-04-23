from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import (
    Tile, TileCalculation, Plywood, PlywoodCalculation,
    ElectricComponent, ElectricalCalculation
)
from .forms import (
    TileForm, TileCalculationForm, PlywoodForm,
    PlywoodCalculationForm, ElectricComponentForm, ElectricalCalculationForm
)


class TileListView(ListView):
    model = Tile
    template_name = 'materiais/tile_list.html'
    context_object_name = 'tiles'


class TileCreateView(CreateView):
    model = Tile
    form_class = TileForm
    template_name = 'materiais/tile_form.html'
    success_url = reverse_lazy('materiais:tile_list')


class TileCalculationListView(ListView):
    model = TileCalculation
    template_name = 'materiais/tile_calculation_list.html'
    context_object_name = 'calculations'


class TileCalculationCreateView(CreateView):
    model = TileCalculation
    form_class = TileCalculationForm
    template_name = 'materiais/tile_calculation_form.html'
    success_url = reverse_lazy('materiais:tile_calculation_list')


class PlywoodListView(ListView):
    model = Plywood
    template_name = 'materiais/plywood_list.html'
    context_object_name = 'plywoods'


class PlywoodCreateView(CreateView):
    model = Plywood
    form_class = PlywoodForm
    template_name = 'materiais/plywood_form.html'
    success_url = reverse_lazy('materiais:plywood_list')


class PlywoodCalculationListView(ListView):
    model = PlywoodCalculation
    template_name = 'materiais/plywood_calculation_list.html'
    context_object_name = 'calculations'


class PlywoodCalculationCreateView(CreateView):
    model = PlywoodCalculation
    form_class = PlywoodCalculationForm
    template_name = 'materiais/plywood_calculation_form.html'
    success_url = reverse_lazy('materiais:plywood_calculation_list')


class ElectricComponentListView(ListView):
    model = ElectricComponent
    template_name = 'materiais/electric_component_list.html'
    context_object_name = 'components'


class ElectricComponentCreateView(CreateView):
    model = ElectricComponent
    form_class = ElectricComponentForm
    template_name = 'materiais/electric_component_form.html'
    success_url = reverse_lazy('materiais:electric_component_list')


class ElectricalCalculationListView(ListView):
    model = ElectricalCalculation
    template_name = 'materiais/electrical_calculation_list.html'
    context_object_name = 'calculations'


class ElectricalCalculationCreateView(CreateView):
    model = ElectricalCalculation
    form_class = ElectricalCalculationForm
    template_name = 'materiais/electrical_calculation_form.html'
    success_url = reverse_lazy('materiais:electrical_calculation_list')


def home(request):
    return render(request, 'materiais/home.html') 