from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import (
    Tile, TileCalculation, Plywood, PlywoodCalculation
)
from .forms import (
    TileForm, TileCalculationForm, PlywoodForm,
    PlywoodCalculationForm
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


class TileUpdateView(UpdateView):
    model = Tile
    form_class = TileForm
    template_name = 'materiais/tile_form.html'
    success_url = reverse_lazy('materiais:tile_list')


class TileDeleteView(DeleteView):
    model = Tile
    template_name = 'materiais/confirm_delete.html'
    success_url = reverse_lazy('materiais:tile_list')
    context_object_name = 'object'


class TileDetailView(DetailView):
    model = Tile
    template_name = 'materiais/tile_detail.html'
    context_object_name = 'tile'


class TileCalculationListView(ListView):
    model = TileCalculation
    template_name = 'materiais/tile_calculation_list.html'
    context_object_name = 'calculations'
    ordering = ['-calculation_date']


class TileCalculationCreateView(CreateView):
    model = TileCalculation
    form_class = TileCalculationForm
    template_name = 'materiais/tile_calculation_form.html'
    success_url = reverse_lazy('materiais:tile_calculation_list')


class TileCalculationUpdateView(UpdateView):
    model = TileCalculation
    form_class = TileCalculationForm
    template_name = 'materiais/tile_calculation_form.html'
    success_url = reverse_lazy('materiais:tile_calculation_list')


class TileCalculationDeleteView(DeleteView):
    model = TileCalculation
    template_name = 'materiais/confirm_delete.html'
    success_url = reverse_lazy('materiais:tile_calculation_list')
    context_object_name = 'object'


class TileCalculationDetailView(DetailView):
    model = TileCalculation
    template_name = 'materiais/tile_calculation_detail.html'
    context_object_name = 'calculation'


class PlywoodListView(ListView):
    model = Plywood
    template_name = 'materiais/plywood_list.html'
    context_object_name = 'plywoods'


class PlywoodCreateView(CreateView):
    model = Plywood
    form_class = PlywoodForm
    template_name = 'materiais/plywood_form.html'
    success_url = reverse_lazy('materiais:plywood_list')


class PlywoodUpdateView(UpdateView):
    model = Plywood
    form_class = PlywoodForm
    template_name = 'materiais/plywood_form.html'
    success_url = reverse_lazy('materiais:plywood_list')


class PlywoodDeleteView(DeleteView):
    model = Plywood
    template_name = 'materiais/confirm_delete.html'
    success_url = reverse_lazy('materiais:plywood_list')
    context_object_name = 'object'


class PlywoodDetailView(DetailView):
    model = Plywood
    template_name = 'materiais/plywood_detail.html'
    context_object_name = 'plywood'


class PlywoodCalculationListView(ListView):
    model = PlywoodCalculation
    template_name = 'materiais/plywood_calculation_list.html'
    context_object_name = 'calculations'
    ordering = ['-calculation_date']


class PlywoodCalculationCreateView(CreateView):
    model = PlywoodCalculation
    form_class = PlywoodCalculationForm
    template_name = 'materiais/plywood_calculation_form.html'
    success_url = reverse_lazy('materiais:plywood_calculation_list')


class PlywoodCalculationUpdateView(UpdateView):
    model = PlywoodCalculation
    form_class = PlywoodCalculationForm
    template_name = 'materiais/plywood_calculation_form.html'
    success_url = reverse_lazy('materiais:plywood_calculation_list')


class PlywoodCalculationDeleteView(DeleteView):
    model = PlywoodCalculation
    template_name = 'materiais/confirm_delete.html'
    success_url = reverse_lazy('materiais:plywood_calculation_list')
    context_object_name = 'object'


class PlywoodCalculationDetailView(DetailView):
    model = PlywoodCalculation
    template_name = 'materiais/plywood_calculation_detail.html'
    context_object_name = 'calculation'


def home(request):
    return render(request, 'materiais/home.html')
