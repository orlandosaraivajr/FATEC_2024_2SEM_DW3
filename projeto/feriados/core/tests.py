from django.test import TestCase

class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'natal')
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'natal.html')


from .models import FeriadoModel
from datetime import datetime

class FeriadoModelTest(TestCase):
    def setUp(self):
        self.cadastro = FeriadoModel(nome='Natal', dia=25, mes=12)
        self.cadastro.save()
    
    def test_created(self):
        self.assertTrue(FeriadoModel.objects.exists())
    
    def test_nome_feriado(self):
        feriado = FeriadoModel.objects.first()
        nome = self.cadastro.__dict__.get('nome')
        self.assertEqual(nome, feriado.nome)
    
    def test_modificado(self):
        feriado = FeriadoModel.objects.first()
        self.assertIsInstance(feriado.modificado_em, datetime)
        self.assertNotIsInstance(feriado.modificado_em, str)