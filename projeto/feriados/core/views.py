from django.shortcuts import render
from django.shortcuts import HttpResponse

def natal(request):
   contexto = {'natal':True}
   return render(request, 'natal.html', contexto)

def api(request):
   return HttpResponse('API')