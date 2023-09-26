from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from PIL import Image
from datetime import datetime

# Create your models here.
class Cambio(models.Model):
    cambio = models.CharField(max_length=20,default='Manual')

    class Meta:
        verbose_name_plural = 'Cambio' 

    def __str__(self):
        return self.cambio
    
class Carroceria(models.Model):
    carroceria = models.CharField(max_length=20,default='Sedã')

    def __str__(self):
        return self.carroceria
    
    class Meta:
        verbose_name_plural = 'Carroceria' 

class Cor(models.Model):
    cor = models.CharField(max_length=20,default='Cinza')

    def __str__(self):
        return self.cor
    
    class Meta:
        verbose_name_plural = 'Cor' 

class Combustivel(models.Model):
    combustivel = models.CharField(default='Gasolina',max_length=20)

    def __str__(self):
        return self.combustivel
    
    class Meta:
        verbose_name_plural = 'Combustivel' 

class Itens_veiculo(models.Model):
    itens_veiculo = models.CharField(max_length=20,default='Airbag')

    def __str__(self):
        return self.itens_veiculo 

    class Meta:
        verbose_name_plural = 'Itens Veiculo'    
 


class Automovel(models.Model):
    nome = models.CharField(default='Carro',max_length=30,null=True, blank=True)
    valor = models.CharField(default='70.000,00',max_length=15,null=True, blank=True)
    versao_carro = models.CharField(default='Versão Nova',max_length=25,null=True, blank=True)
    marca = models.CharField(default='Sem Marca',max_length=25,null=True, blank=True)
    cidade = models.CharField(default='Americana', max_length=50,null=True, blank=True)
    estado = models.CharField(default='São Paulo', max_length=50,null=True, blank=True)
    ano = models.CharField(default='2024',max_length=4,null=True, blank=True)
    km = models.CharField(default='0',max_length=6,null=True, blank=True)
    placa = models.CharField(default='999-999',max_length=8,null=True, blank=True)
    nome_loja = models.CharField(default='Loja Veiculos',max_length=30,null=True, blank=True)
    ipva_pago = models.BooleanField(default=True)
    sobre_automovel = models.TextField(default='Sobre')
    cambio = models.ManyToManyField(Cambio,default='Manual',blank=True)
    carroceria = models.ManyToManyField(Carroceria, blank=True)
    combustivel = models.ManyToManyField(Combustivel,default='Flex', blank=True)
    cor = models.ManyToManyField(Cor,default='Cinza', blank=True)
    aceita_troca = models.BooleanField(default=True)
    licenciado = models.BooleanField(default=True)
    foto1 = models.ImageField(default='default.jpg',upload_to='media',null=True, blank=True)
    foto2 = models.ImageField(default='default.jpg',upload_to='media',null=True, blank=True)
    foto3 = models.ImageField(default='default.jpg',upload_to='media',null=True, blank=True)
    foto4 = models.ImageField(default='default.jpg',upload_to='media',null=True, blank=True)
    foto5 = models.ImageField(default='default.jpg',upload_to='media',null=True, blank=True)
    itens_veiculo = models.ManyToManyField(Itens_veiculo)
    contato = models.CharField(max_length=30,default='(19)99999-9999')
    login = models.ForeignKey(User, on_delete=models.CASCADE, default=User.username, null=False, blank=False)
    status_anuncio = models.BooleanField(default=True)
    data_criado = models.DateTimeField(default=timezone.now)
    viram_anuncio = models.IntegerField(default=0)
    vezes_na_lista = models.IntegerField(default=0) 

    favoritos = models.ManyToManyField(User,related_name='Favorito',default=None,blank=True)

    #Prevent to show extra 'S' on the names
    class Meta:
        verbose_name_plural = 'Anuncio Automovel'

    def __str__(self):
        return self.nome    
    

class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name   
    
    
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)    

    def __str__(self):
        return self.user   