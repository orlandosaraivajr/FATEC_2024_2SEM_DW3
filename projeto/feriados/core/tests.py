from django.test import TestCase
from .models import FeriadoModel
from datetime import datetime

class Feriado_no_holiday_Test(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Não temos feriado hoje.')
        self.assertContains(self.resp, 'Vamos para aula.')
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'feriado.html')

class Feriado_one_holiday_Test(TestCase):
    def setUp(self):
        self.feriado = 'Melhor aula'
        hoje = datetime.today()
        FeriadoModel.objects.create(nome=self.feriado,dia=hoje.day,mes=hoje.month)
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, self.feriado)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'feriado.html')


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


from core.forms import FeriadoForm

class FeriadoFormTest(TestCase):
    def test_form_has_fields(self):
        form = FeriadoForm()
        expected = ['nome', 'dia', 'mes']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_must_be_capitalized(self):
        dados = {'nome':'Tiradentes', 'dia':14,'mes':4}
        form = FeriadoForm(dados)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['nome'], 'Tiradentes'.upper())
    
    def test_month_between_1_and_12__001(self):
        dados = {'nome':'Tiradentes', 'dia':14,'mes':4}
        form = FeriadoForm(dados)
        self.assertTrue(form.is_valid())
        self.assertEqual({}, form.errors)
        self.assertEqual(form.cleaned_data['mes'], 4)
        
    def test_month_between_1_and_12__error(self):
        dados = {'nome':'Tiradentes', 'dia':14,'mes':0}
        form = FeriadoForm(dados)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors.get('mes')[0], 'Mês inválido')
    
    def test_month_between_1_and_12__error2(self):
        dados = {'nome':'Tiradentes', 'dia':14,'mes':13}
        form = FeriadoForm(dados)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors.get('mes')[0], 'Mês inválido')

    def test_day_between_1_and_31__001(self):
        dados = {'nome':'Tiradentes', 'dia':1,'mes':4}
        form = FeriadoForm(dados)
        self.assertTrue(form.is_valid())
        self.assertEqual({}, form.errors)
        self.assertEqual(form.cleaned_data['dia'], 1)

    def test_day_between_1_and_31__001(self):
        dados = {'nome':'Tiradentes', 'dia':0,'mes':4}
        form = FeriadoForm(dados)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors.get('dia')[0], 'Dia inválido')