from django.db import models

class Tecnico(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=14)
    equipe = models.OneToOneField("equipes.Equipe", on_delete=models.CASCADE, related_name="tecnico")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Técnico"
        verbose_name_plural = "Técnicos"
