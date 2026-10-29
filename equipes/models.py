from django.db import models

class Equipe(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    curso = models.CharField(max_length=100)
    cor = models.CharField(max_length=7)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"
        ordering = ['nome']
