from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramSerializerTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo='Procurando ninguém',
            data_lancamento='2007-07-04',
            tipo='F',
            likes=123,
            dislikes=23,
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifica_campos_serializados(self):
        """ teste de verificação dos campos serializados """
        data = self.serializer.data
        self.assertEquals(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))

    def test_verifica_conteudo_campos_serializados(self):
        data = self.serializer.data
        self.assertEquals(data['titulo'], self.programa.titulo)
        self.assertEquals(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEquals(data['tipo'], self.programa.tipo)
        self.assertEquals(data['likes'], self.programa.likes)
