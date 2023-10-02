from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from PIL import Image
from datetime import datetime

# Create your models here.
class Cambio(models.Model):
    cambio = models.CharField(max_length=20,default='Manual', blank=False)

    class Meta:
        verbose_name_plural = 'Cambio' 

    def __str__(self):
        return self.cambio
    
class Carroceria(models.Model):
    carroceria = models.CharField(max_length=20,default='Sedã', blank=False)

    def __str__(self):
        return self.carroceria
    
    class Meta:
        verbose_name_plural = 'Carroceria' 

class Cor(models.Model):
    cor = models.CharField(max_length=30,default='Cinza', null=False, blank=False)

    def __str__(self):
        return self.cor
    
    class Meta:
        verbose_name_plural = 'Cor' 

class Combustivel(models.Model):
    combustivel = models.CharField(default='Gasolina',max_length=20, blank=False)

    def __str__(self):
        return self.combustivel
    
    class Meta:
        verbose_name_plural = 'Combustivel' 

class Itens_veiculo(models.Model):
    itens_veiculo = models.CharField(max_length=50,default='Airbag', null=False, blank=False)

    def __str__(self):
        return self.itens_veiculo 

    class Meta:
        verbose_name_plural = 'Itens Veiculo'    


class TipoAutomovel(models.Model):
    tipo_automovel = models.CharField(max_length=20,default='Carro ou Moto...', null=False, blank=False)

    def __str__(self):
        return self.tipo_automovel 

    class Meta:
        verbose_name_plural = 'Tipo de Automóvel'

class MarcaAutomovel(models.Model):
    marca_automovel = models.CharField(max_length=20,default='Honda', null=False, blank=False)

    def __str__(self):
        return self.marca_automovel 

    class Meta:
        verbose_name_plural = 'Marca Automóvel' 


class Automovel(models.Model):
    nome = models.CharField(default='Carro',max_length=30,null=False, blank=False)
    tipo_automovel = models.ManyToManyField(TipoAutomovel,blank=False)
    valor = models.CharField(default='10.000,00',max_length=15,null=False, blank=False)
    versao_carro = models.CharField(default='2.0 2023',max_length=50,null=False, blank=False)
    marca = models.ManyToManyField(MarcaAutomovel,blank=False)
    cidade = models.CharField(default='Americana', max_length=50,null=False, blank=False)
    estado = models.CharField(default='São Paulo', max_length=50,null=False, blank=False)
    ano = models.CharField(default='2024',max_length=4,null=False, blank=False)
    km = models.CharField(default='0',max_length=6,null=False, blank=False)
    placa = models.CharField(default='999-999',max_length=8,null=False, blank=False)
    nome_loja = models.CharField(default='Loja Veiculos',max_length=30,null=False, blank=False)
    ipva_pago = models.BooleanField(default=True)
    sobre_automovel = models.TextField(default='EXTREMAMENTE NOVO! Outros Opcionais: Farol de neblina, Direção Elétrica, Comando de áudio no volante, Controle de estabilidade, Distribuição eletrônica de frenagem, Kit Multimídia, Pára-choques na cor do veículo.',null=False, blank=False)
    cambio = models.ManyToManyField(Cambio,default='Manual', blank=False)
    carroceria = models.ManyToManyField(Carroceria, blank=False)
    combustivel = models.ManyToManyField(Combustivel,default='Flex', blank=False)
    cor = models.ManyToManyField(Cor,default='Cinza', blank=False)
    aceita_troca = models.BooleanField(default=True)
    licenciado = models.BooleanField(default=True)
    foto1 = models.ImageField(default='default.jpg',upload_to='media',null=False, blank=False)
    foto2 = models.ImageField(default='default.jpg',upload_to='media',null=False, blank=False)
    foto3 = models.ImageField(default='default.jpg',upload_to='media',null=False, blank=False)
    foto4 = models.ImageField(default='default.jpg',upload_to='media',null=False, blank=False)
    foto5 = models.ImageField(default='default.jpg',upload_to='media',null=False, blank=False)
    itens_veiculo = models.ManyToManyField(Itens_veiculo, blank=False)
    contato = models.CharField(max_length=30,default='(19)99999-9999',null=False, blank=False)
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
    created_by = models.CharField(max_length=1000)
    receiver = models.CharField(max_length=1000)
    carro = models.CharField(max_length=1000)

    def __str__(self):
        return self.name   
    
    
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)  
    created_by = models.CharField(max_length=1000)
    receiver = models.CharField(max_length=1000)  

    def __str__(self):
        return self.user   