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
from django.contrib.auth.mixins import LoginRequiredMixin


class TileListView(ListView):
    model = Tile
    template_name = 'materiais/tile_list.html'
    context_object_name = 'tiles'


class TileCreateView(CreateView):
    model = Tile
    form_class = TileForm
    template_name = 'materiais/tile_form.html'
    success_url = reverse_lazy('materiais:tile_list')


class TileUpdateView(LoginRequiredMixin, UpdateView):
    model = Tile
    form_class = TileForm
    template_name = 'materiais/tile_form.html'
    success_url = reverse_lazy('materiais:tile_list')


class TileDeleteView(LoginRequiredMixin, DeleteView):
    model = Tile
    template_name = 'materiais/confirm_delete.html'
    success_url = reverse_lazy('materiais:tile_list')
    context_object_name = 'object'


class TileDetailView(DetailView):
    model = Tile
    template_name = 'materiais/view_details.html'
    context_object_name = 'object'


class TileCalculationListView(ListView):
    model = TileCalculation
    template_name = 'materiais/tile_calculation_list.html'
    context_object_name = 'calculations'
    ordering = ['-calculation_date']

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(user=self.request.user)
        return qs.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calculations = context['calculations']
        tile_calcs = [c for c in calculations if c.tile.type == 'tile']
        pvc_calcs = [c for c in calculations if c.tile.type == 'pvc']
        context['total_tile_boxes'] = sum(c.total_boxes for c in tile_calcs)
        context['total_tile_cost'] = sum(c.total_cost for c in tile_calcs)
        context['total_pvc_boxes'] = sum(c.total_boxes for c in pvc_calcs)
        context['total_pvc_cost'] = sum(c.total_cost for c in pvc_calcs)
        context['total_cost'] = sum(calc.total_cost for calc in calculations)
        return context


class TileCalculationCreateView(LoginRequiredMixin, CreateView):
    model = TileCalculation
    form_class = TileCalculationForm
    template_name = 'materiais/tile_calculation_form.html'
    success_url = reverse_lazy('materiais:tile_calculation_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TileCalculationUpdateView(LoginRequiredMixin, UpdateView):
    model = TileCalculation
    form_class = TileCalculationForm
    template_name = 'materiais/tile_calculation_form.html'
    success_url = reverse_lazy('materiais:tile_calculation_list')


class TileCalculationDeleteView(LoginRequiredMixin, DeleteView):
    model = TileCalculation
    template_name = 'materiais/confirm_delete.html'
    success_url = reverse_lazy('materiais:tile_calculation_list')
    context_object_name = 'object'


class TileCalculationDetailView(DetailView):
    model = TileCalculation
    template_name = 'materiais/view_details.html'
    context_object_name = 'object'


class PlywoodListView(ListView):
    model = Plywood
    template_name = 'materiais/plywood_list.html'
    context_object_name = 'plywoods'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(user=self.request.user)
        return qs.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plywoods = context['plywoods']
        context['total_plywood_sheet'] = sum(c.total_sheets for c in plywoods)
        context['total_plywood_cost'] = sum(c.total_cost for c in plywoods)
        context['total_cost'] = sum(calc.total_cost for calc in plywoods)
        return context


class PlywoodCreateView(CreateView):
    model = Plywood
    form_class = PlywoodForm
    template_name = 'materiais/plywood_form.html'
    success_url = reverse_lazy('materiais:plywood_list')


class PlywoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Plywood
    form_class = PlywoodForm
    template_name = 'materiais/plywood_form.html'
    success_url = reverse_lazy('materiais:plywood_list')


class PlywoodDeleteView(LoginRequiredMixin, DeleteView):
    model = Plywood
    template_name = 'materiais/confirm_delete.html'
    success_url = reverse_lazy('materiais:plywood_list')
    context_object_name = 'object'


class PlywoodDetailView(DetailView):
    model = Plywood
    template_name = 'materiais/view_details.html'
    context_object_name = 'object'


class PlywoodCalculationListView(ListView):
    model = PlywoodCalculation
    template_name = 'materiais/plywood_calculation_list.html'
    context_object_name = 'calculations'
    ordering = ['-calculation_date']


class PlywoodCalculationCreateView(LoginRequiredMixin, CreateView):
    model = PlywoodCalculation
    form_class = PlywoodCalculationForm
    template_name = 'materiais/plywood_calculation_form.html'
    success_url = reverse_lazy('materiais:plywood_calculation_list')


class PlywoodCalculationUpdateView(LoginRequiredMixin, UpdateView):
    model = PlywoodCalculation
    form_class = PlywoodCalculationForm
    template_name = 'materiais/plywood_calculation_form.html'
    success_url = reverse_lazy('materiais:plywood_calculation_list')


class PlywoodCalculationDeleteView(LoginRequiredMixin, DeleteView):
    model = PlywoodCalculation
    template_name = 'materiais/confirm_delete.html'
    success_url = reverse_lazy('materiais:plywood_calculation_list')
    context_object_name = 'object'


class PlywoodCalculationDetailView(DetailView):
    model = PlywoodCalculation
    template_name = 'materiais/view_details.html'
    context_object_name = 'object'


def home(request):
    return render(request, 'materiais/home.html')
