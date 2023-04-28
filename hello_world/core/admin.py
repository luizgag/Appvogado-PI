from django.contrib import admin
from .models import Advogado,Cliente,Depoimento,Compromisso

# Register the Lawyer model to the admin interface
admin.site.register(Advogado)
admin.site.register(Cliente)
admin.site.register(Depoimento)
admin.site.register(Compromisso)