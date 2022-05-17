from builtins import property
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import DateInput, ModelForm, ModelChoiceField, Form, Select, TextInput
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-height', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-height', 'placeholder': 'Contraseña'}))

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class UsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=140, required=True,widget=forms.TextInput(attrs={'class': 'form-control input-height','placeholder':'Usuario'}))
    first_name = forms.CharField(max_length=140, required=True,widget=forms.TextInput(attrs={'class': 'form-control input-height','placeholder':'Nombre'}))
    last_name = forms.CharField(max_length=140, required=False, widget=forms.TextInput(attrs={'class': 'form-control input-height','placeholder':'Apellido'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-height','placeholder':'Contraseña'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-height','placeholder':'Confirmar Contraseña'}))    
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control input-height','placeholder':'email'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'


class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'cli': Select(attrs={
                'class': 'form-control  ',
                'style': 'width: 100%'
            }),
            'date_joined': DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'date_joined',
                    'data-target': '#date_joined',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'iva': TextInput(attrs={
                'class': 'form-control',
            }),
            'subtotal': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'total': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            })
        }

       


class DetSaleForm(forms.ModelForm): 


    class Meta:
        model = DetSale
        fields = '__all__'
       