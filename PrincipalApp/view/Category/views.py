from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView
from PrincipalApp.models import *
from PrincipalApp.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt




class ListarCategoria(ListView):
    template_name = 'Categoria/ListarCategoria.html'
    model = Category
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Category.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categoria'
        return context

class CrearCategoria(CreateView):
    template_name = 'Categoria/CrearCategoria.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('Merlin:ListarCategoria')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

class UpdateCategoria(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'Categoria/UpdateCategoria.html'
    success_url = reverse_lazy('Merlin:ListarCategoria') 

class DeleteCategoria(DeleteView):
    model = Category
    template_name = 'Categoria/DeleteCategoria.html'
    success_url = reverse_lazy('Merlin:ListarCategoria')
