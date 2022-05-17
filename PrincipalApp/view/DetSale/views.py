from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView
from PrincipalApp.models import *
from PrincipalApp.forms import *
from django.urls import reverse_lazy
from django.contrib import messages

  
class ListarDetVenta(ListView):
    template_name = 'DetalleVenta/ListarDetVenta.html'
    model = DetSale

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Detalle Venta'
        return context

class CrearDetVenta(CreateView):
    template_name = 'DetalleVenta/CrearDetVenta.html'
    model = DetSale
    form_class = DetSaleForm
    success_url = reverse_lazy('Merlin:ListarDetVenta')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

class UpdateDetVenta(UpdateView):
    model = DetSale
    form_class = DetSaleForm
    template_name = 'DetalleVenta/UpdateDetVenta.html'
    success_url = reverse_lazy('Merlin:ListarDetVenta') 

class DeleteDetVenta(DeleteView):
    model = DetSale
    template_name = 'DetalleVenta/DeleteDetVenta.html'
    success_url = reverse_lazy('Merlin:ListarDetVenta')