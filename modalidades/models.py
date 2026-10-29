from django.db import models

class Modalidade(models.Model):
    ESCOLHA_TIPO = {
    "C": "Coletiva",
    "I": "Individual"
    }
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=2, choices=ESCOLHA_TIPO)
    max_atletas = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Modalidade"
        verbose_name_plural = "Modalidades"
        ordering = ['nome']
