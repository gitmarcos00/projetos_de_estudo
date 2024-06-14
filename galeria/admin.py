from django.contrib import admin
from galeria.models import Fotografia

# A classe serve para configurar os campos do admin
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "categoria", "publicada") # Quais campos serão exibidos
    list_display_links = ("id", "nome") # Quais campos serão links
    search_fields = ("nome",) # Campo de busca
    list_filter = ("categoria",) # Filtros por CATEGORIAS
    list_editable = ("publicada", ) # Aqui vamos alterar para que seja um check box editável
    list_per_page = 10 # Paginação

admin.site.register(Fotografia, ListandoFotografias)

