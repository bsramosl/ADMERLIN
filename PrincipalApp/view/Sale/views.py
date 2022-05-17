from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView
from PrincipalApp.models import *
from PrincipalApp.forms import *
from django.urls import reverse_lazy
from django.contrib import messages




class ListarVenta(ListView):
    template_name = 'Venta/ListarVenta.html'
    model = Sale

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Venta'
        return context

class CrearVenta(CreateView):
    template_name = 'Venta/CrearVenta.html'
    model = Sale
    form_class = SaleForm
    success_url = reverse_lazy('Merlin:ListarVenta')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

class UpdateVenta(UpdateView):
    model = Sale
    form_class = SaleForm
    template_name = 'Venta/UpdateVenta.html'
    success_url = reverse_lazy('Merlin:ListarVenta') 

class DeleteVenta(DeleteView):
    model = Sale
    template_name = 'Venta/DeleteVenta.html'
    success_url = reverse_lazy('Merlin:ListarVenta')

