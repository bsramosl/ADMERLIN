import datetime
from datetime import date
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import HttpResponseRedirect, request, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import login, logout, update_session_auth_hash
from .models import *
from .forms import *
 

class Login(FormView):
    template_name = 'principal/Login.html'
    form_class = LoginForm
    success_url = reverse_lazy('Merlin:Inicio')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, 'Iniciado sesión con éxito')
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))


class Logout(RedirectView):
    pattern_name = 'Merlin:Login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

 

class Registro(CreateView):
    model = User
    form_class = UsuarioForm
    template_name = 'principal/Registro.html'
    success_url = reverse_lazy('Merlin:Login') 

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response
 
 
class Inicio(TemplateView):
    template_name = 'principal/Inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = Category.objects.count()
        context['producto'] = Product.objects.count()
        context['cliente'] = Client.objects.count()
        return context
   
 
class Venta(CreateView):
    template_name = 'Principal/Venta.html'
    model = Sale
    form_class = SaleForm
    success_url = reverse_lazy('Merlin:ListarDetVenta') 
    

   