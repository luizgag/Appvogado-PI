from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    senha = models.CharField(max_length=128)
    tipo = None

    class Meta:
        # abstract = True
        app_label = 'core'


class Advogado(Usuario):

    especialidade = models.CharField(max_length=100)
    sobre = models.TextField()
    anos_experiencia = models.IntegerField()
    tipo = 'Advogado'

    class Meta:
        app_label = 'core'

class Cliente(Usuario):

    tipo = 'Cliente'

    class Meta:
        app_label = 'core'

class Depoimento(models.Model):
    texto = models.TextField()

    #cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.text[:50]
    
    class Meta:
        app_label = 'core'

class Compromisso(models.Model):
    data_horario = models.DateTimeField()
    advogado = models.ForeignKey(Advogado,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,blank=True,null=True)
    descricao = models.TextField(blank=True)

    class Meta:
        app_label = 'core'
  