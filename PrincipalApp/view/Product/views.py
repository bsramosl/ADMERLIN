from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView
from PrincipalApp.models import *
from PrincipalApp.forms import *
from django.urls import reverse_lazy
from django.contrib import messages


class ListarProducto(ListView):
    template_name = 'Producto/ListarProducto.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Producto'
        return context

class CrearProducto(CreateView):
    template_name = 'Producto/CrearProducto.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('Merlin:ListarProducto')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

class UpdateProducto(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'Producto/UpdateProducto.html'
    success_url = reverse_lazy('Merlin:ListarProducto') 

class DeleteProducto(DeleteView):
    model = Product
    template_name = 'Producto/DeleteProducto.html'
    success_url = reverse_lazy('Merlin:ListarProducto')


