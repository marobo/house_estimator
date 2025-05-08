from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import (
    Tile, Plywood,
    ElectricComponent, Calculation
)
from .forms import (
    TileForm, PlywoodForm, ElectricComponentForm, CalculationForm
)
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse


class TileListView(ListView):
    model = Tile
    template_name = 'materiais/generic_list.html'
    context_object_name = 'context_objects'
    ordering = ['-name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tiles and PVC'
        context['name'] = 'Name'
        context['size'] = 'Size (cm)'
        context['pieces_per_box'] = 'Pieces per Box'
        context['price_per_box'] = 'Price per Box'
        context['area_per_piece'] = 'Area per Piece (m²)'
        context['waste_percentage'] = 'Waste %'
        context['actions'] = 'Actions'
        return context


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



class PlywoodListView(ListView):
    model = Plywood
    template_name = 'materiais/generic_list.html'
    context_object_name = 'context_objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Plywood'
        context['name'] = 'Name'
        context['size'] = 'Size (m)'
        context['area_per_sheet'] = 'Area (m²)'
        context['price_per_sheet'] = 'Price per Sheet'
        context['actions'] = 'Actions'
        return context


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


class ElectricComponentListView(ListView):
    model = ElectricComponent
    template_name = 'materiais/generic_list.html'
    context_object_name = 'context_objects'


class ElectricComponentCreateView(CreateView):
    model = ElectricComponent
    form_class = ElectricComponentForm
    template_name = 'materiais/electric_component_form.html'
    success_url = reverse_lazy('materiais:electric_component_list')


class ElectricComponentDetailView(DetailView):
    model = ElectricComponent
    template_name = 'materiais/electric_component_detail.html'
    context_object_name = 'component'


class ElectricComponentUpdateView(UpdateView):
    model = ElectricComponent
    form_class = ElectricComponentForm
    template_name = 'materiais/electric_component_form.html'
    success_url = reverse_lazy('materiais:electric_component_list')


class ElectricComponentDeleteView(DeleteView):
    model = ElectricComponent
    template_name = 'materiais/confirm_delete.html'
    success_url = reverse_lazy('materiais:electric_component_list')
    context_object_name = 'object'


class CalculationListView(ListView):
    model = Calculation
    template_name = 'materiais/calculation_list.html'
    context_object_name = 'calculations'
    ordering = ['-calculation_date']


class CalculationCreateView(CreateView):
    model = Calculation
    form_class = CalculationForm
    template_name = 'materiais/calculation_form.html'
    success_url = reverse_lazy('materiais:calculation_list')

    def form_valid(self, form):
        # Set content_type and object_id based on selected material
        category = form.cleaned_data['category']
        material = form.cleaned_data['material']
        if category == 'tile':
            form.instance.content_type = ContentType.objects.get_for_model(Tile)
        elif category == 'plywood':
            form.instance.content_type = ContentType.objects.get_for_model(Plywood)
        elif category == 'electrical':
            form.instance.content_type = ContentType.objects.get_for_model(ElectricComponent)
        form.instance.object_id = material.id
        return super().form_valid(form)


class CalculationUpdateView(UpdateView):
    model = Calculation
    form_class = CalculationForm
    template_name = 'materiais/calculation_form.html'
    success_url = reverse_lazy('materiais:calculation_list')

    def form_valid(self, form):
        category = form.cleaned_data['category']
        material = form.cleaned_data['material']
        if category == 'tile':
            form.instance.content_type = ContentType.objects.get_for_model(Tile)
        elif category == 'plywood':
            form.instance.content_type = ContentType.objects.get_for_model(Plywood)
        elif category == 'electrical':
            form.instance.content_type = ContentType.objects.get_for_model(ElectricComponent)
        form.instance.object_id = material.id
        return super().form_valid(form)


class CalculationDetailView(DetailView):
    model = Calculation
    template_name = 'materiais/calculation_detail.html'
    context_object_name = 'calculation'


class CalculationDeleteView(DeleteView):
    model = Calculation
    template_name = 'materiais/confirm_delete.html'
    success_url = reverse_lazy('materiais:calculation_list')
    context_object_name = 'object'


def home(request):
    return render(request, 'materiais/home.html')


def get_materials(request):
    category = request.GET.get('category')
    data = []
    if category == 'tile':
        data = list(Tile.objects.values('id', 'name'))
    elif category == 'plywood':
        data = list(Plywood.objects.values('id', 'name'))
    elif category == 'electrical':
        data = list(ElectricComponent.objects.values('id', 'name'))
    return JsonResponse({'materials': data})
