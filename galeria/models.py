from django.db import models
from datetime import datetime

OPCOES_CATEGORIA = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
    ]

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(max_length=100, null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True ) # Alteração para salvar os arquivos
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self) -> str:
        return f"Fotografia [nome={self.nome}]"

