from django.db import models

# Create your models here.

# Criação da Model Grupo e seus atributos
class Grupo(models.Model):

    nome = models.CharField("Nome do Grupo", max_length=100, unique=True)
    debut = models.DateField("Debut do Grupo")
    resumo = models.TextField("Resumo do Grupo")
    #comeback = models.ForeignKey(Comeback, on_delete=models.CASCADE)
    #member = models.ManyToManyField(Integrante, verbose_name="list of sites")
    #imagem = models.ImageField("Foto do Grupo")

    def __str__(self):
        return self.nome

# Criação da Model Artista e seus atributos
class Artista(models.Model):

    nome = models.CharField("Nome do Artista", max_length=100, unique=True)
    # ForeignKey vai associar um grupo ao artista criado: o artista N é do grupo X
    grupo = models.ForeignKey(Grupo, verbose_name="Grupo do Artista", on_delete=models.CASCADE)
    idade = models.PositiveIntegerField("Idade do Artista")
    GENDER_CHOICES = ((u'M', u'Masculino'),
                      (u'F', u'Feminino'),)
    genero = models.CharField(max_length=2, verbose_name="Gênero do Artista", choices=GENDER_CHOICES)
    pais = models.CharField("País do Artista", max_length=100)
    #imagem = models.ImageField("Foto do Artista")

    def __str__(self):
        return self.nome

# Criação da Model Comeback e seus atributos
class Comeback(models.Model):

    nome = models.CharField("Nome da Música", max_length = 100, unique=True)
    # ForeignKey vai associar um grupo ao comeback criado: o comeback N é do grupo X
    grupo = models.ForeignKey(Grupo, verbose_name="Grupo do Artista", on_delete=models.CASCADE)
    data = models.DateField("Data do Música")
    views = models.PositiveIntegerField("Número de Views")
    likes = models.PositiveIntegerField("Número de Likes")
    deslikes = models.PositiveIntegerField("Número de Deslikes")

    def __str__(self):
        return self.nome    