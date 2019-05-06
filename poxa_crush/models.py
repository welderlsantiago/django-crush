from django.db import models

# Create your models here.
class Crush(models.Model):
    signo_opcoes =[
        ('aries', 'áries'),
        ('touro', 'touro'),
        ('gemeos', 'gêmeos'),
        ('cancer', 'cancêr'),
        ('leao', 'leão'),
        ('virgem', 'virgem'),
        ('libra', 'libra'),
        ('escorpiao', 'escorpião'),
        ('sagitario', 'sagitário'),
        ('capricornio', 'capricórnio'),
        ('aquario', 'aquário'),
        ('peixes', 'peixes')
    ]

    def __str__ (self):
        return self.nome


    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    data = models.DateField()
    signo = models.CharField(max_length=15, choices=signo_opcoes)
    qualidade = models.CharField(max_length=100)
    defeito = models.CharField(max_length=100, default= 'não está comigo')
    reciproco = models.BooleanField(default=False)
    solteiro = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='', null=True)