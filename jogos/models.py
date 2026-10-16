from django.db import models

from django.db import models


class Modalidade(models.Model):
    ESCOLHA_TIPO = {
    "coletiva": "coletiva",
    "individual": "individual"
    }
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=12, choices=ESCOLHA_TIPO)
    max_atletas = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Modalidade"
        verbose_name_plural = "Modalidades"
        ordering = ['nome']

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

class Tecnico(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=14)
    equipe = models.OneToOneField(Equipe, on_delete=models.CASCADE, related_name="tecnico")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Técnico"
        verbose_name_plural = "Técnicos"

class Atleta(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT, related_name="atletas")
    modalidade = models.ManyToManyField(Modalidade, related_name="atleta", blank=True)


    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Atleta"
        verbose_name_plural = "Atletas"
        ordering = ['nome']
