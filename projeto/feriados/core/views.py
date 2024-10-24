from django.shortcuts import render
from django.shortcuts import HttpResponse
from core.models import FeriadoModel
from datetime import date

def index(request):
   # import ipdb; ipdb.set_trace()
   hoje = date.today()
   feriado = FeriadoModel.objects.filter(mes=hoje.month, dia=hoje.day)
   
   contexto = {'feriado':False}
   if len(feriado) > 0:
      contexto = {'feriado':True, 'nome_feriado':feriado[0].nome}
   return render(request, 'feriado.html', contexto)

def api(request):
   return HttpResponse('API')

from core.services import inserir_mongo
import datetime
def mongo(request):
   dados_inserir = { "author": "Orlando",
    "text": "Django e mongo juntos!",
    "tags": ["mongodb", "python", "pymongo", "django"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
   }
   inserido = inserir_mongo(dados_inserir)
   return HttpResponse(inserido)