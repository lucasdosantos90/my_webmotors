from django.contrib import admin
from .models import Automovel, Cambio, Carroceria, Cor, Combustivel, Itens_veiculo, Room, Message

# Register your models here.
admin.site.register(Automovel)
admin.site.register(Cambio)
admin.site.register(Carroceria)
admin.site.register(Cor)
admin.site.register(Combustivel)
admin.site.register(Itens_veiculo)
admin.site.register(Room)
admin.site.register(Message)