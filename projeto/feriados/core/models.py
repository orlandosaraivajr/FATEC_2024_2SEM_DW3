from django.db import models

class FeriadoModel(models.Model):
    nome = models.CharField('Feriado', max_length=50)
    dia = models.IntegerField('dia')
    mes = models.IntegerField('mes')
    modificado_em = models.DateTimeField(verbose_name='modificado_em',
                                         auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.nome