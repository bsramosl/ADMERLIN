from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView
from PrincipalApp.models import *
from PrincipalApp.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



class ListarCliente(ListView):
    template_name = 'Cliente/ListarCliente.html'
    model = Client

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
 
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cliente'
        return context

class CrearCliente(CreateView):
    template_name = 'Cliente/CrearCliente.html'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('Merlin:ListarCliente')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

class UpdateCliente(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'Cliente/UpdateCliente.html'
    success_url = reverse_lazy('Merlin:ListarCliente') 

class DeleteCliente(DeleteView):
    model = Client
    template_name = 'Cliente/DeleteCliente.html'
    success_url = reverse_lazy('Merlin:ListarCliente')
 
 