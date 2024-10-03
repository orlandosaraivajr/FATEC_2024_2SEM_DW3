from django.shortcuts import render
from django.shortcuts import HttpResponse
from core.models import FeriadoModel
from datetime import datetime

def index(request):
   hoje = datetime.today()
   feriado = FeriadoModel.objects.filter(mes=hoje.month)
   feriado = feriado.filter(dia=hoje.day)
   # import ipdb; ipdb.set_trace()
   if len(feriado) > 0:
      contexto = {'feriado':True, 'nome_feriado':feriado[0].nome}
   else:
      contexto = {'feriado':False}
   return render(request, 'feriado.html', contexto)

def api(request):
   return HttpResponse('API')