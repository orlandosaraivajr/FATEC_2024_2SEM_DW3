from django.shortcuts import render
from django.shortcuts import HttpResponse
from core.models import FeriadoModel
from datetime import datetime

def index(request):
   hoje = datetime.today()
   feriado = FeriadoModel.objects.filter(mes=hoje.month, dia=hoje.day)
   # import ipdb; ipdb.set_trace()
   contexto = {'feriado':False}
   if len(feriado) > 0:
      contexto = {'feriado':True, 'nome_feriado':feriado[0].nome}
   return render(request, 'feriado.html', contexto)

def api(request):
   return HttpResponse('API')