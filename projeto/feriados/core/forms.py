from django import forms 
from django.core.exceptions import ValidationError

class FeriadoForm(forms.Form):
    nome = forms.CharField()
    dia = forms.IntegerField()
    mes = forms.IntegerField()

    def clean_nome(self):
        return self.cleaned_data['nome'].upper()
    
    def clean_mes(self):
        mes = self.cleaned_data['mes']
        if mes > 12 or mes < 1:
            raise ValidationError('Mês inválido')
        return mes

    def clean_dia(self):
        dia = self.cleaned_data['dia']
        if dia > 31 or dia < 1:
            raise ValidationError('Dia inválido')
        return dia