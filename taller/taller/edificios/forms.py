from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from edificios.models import Edificio, \
        Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese direccion por favor'),
            'ciudad': _('Ingrese ciudad por favor'),
            'tipo': _('Ingrese tipo por favor'),
        }

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        if valor[0] == "L":
            raise forms.ValidationError("El nombre de la ciudad no puede iniciar con la letra mayúscula L")
        return valor

    # Agregar clases de Bootstrap en el formulario.
    def __init__(self, *args, **kwargs):
        super(EdificioForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo', 'num_cuartos', 'edificio']

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if valor > 100000:
            raise forms.ValidationError("El costo del departamento no puede ser mayor a $100 mil.")
        return valor
    def clean_num_cuartos(self):
        valor = self.cleaned_data['num_cuartos']
        if valor == 0:
            raise forms.ValidationError("El número de cuartos no puede ser 0.")
        if valor > 7:
            raise forms.ValidationError("El número de cuartos no puede ser mayor a 7.")
        return valor

    def clean_nombre_propietario(self):
        valor = self.cleaned_data['nombre_propietario']
        num_palabras = len(valor.split())
        if num_palabras < 3:
            raise forms.ValidationError("Ingrese tres nombre por favor")
        return valor
    
    # Agregar clases de Bootstrap en el formulario.
    def __init__(self, *args, **kwargs):
        super(DepartamentoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo', 'num_cuartos', 'edificio']
