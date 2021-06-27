from django.contrib import admin

# Importar las clases del modelo
from edificios.models import Edificio, Departamento

class EdificioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'direccion')

admin.site.register(Edificio, EdificioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('nombre_propietario', 'costo', 'num_cuartos', 'edificio')
    raw_id_fields = ('edificio',)

admin.site.register(Departamento, DepartamentoAdmin)

