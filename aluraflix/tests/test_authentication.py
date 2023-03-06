from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase


class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('c3po', password='12345')

    def test_autenticao_user_com_credenciais_corretas(self):
        """ Teste de verificação de autenticação de usuario com credencias corretas """
        user = authenticate(username='c3po', password='12345')
        self.assertTrue((user is not None) and user.is_authenticated)