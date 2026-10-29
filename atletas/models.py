from django.db import models

class Atleta(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    equipe = models.ForeignKey("equipes.Equipe", on_delete=models.PROTECT, related_name="atletas")
    modalidade = models.ManyToManyField("modalidades.Modalidade", related_name="atleta", blank=True)


    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Atleta"
        verbose_name_plural = "Atletas"
        ordering = ['nome']
