from django.test import TestCase
from _datetime import datetime
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.


class PostModelTest(TestCase):
    def test_create(self):
        user = User.objects.create(
            username='test', email='gustavo@gmail.com', password='nick_pass')
        Post.objects.create(
            author=user,
            title='Teste 01',
            subtitle='Realizando teste de número 01',
            text='Texto texto texto texto',
            created_date=datetime.now(),
        )
        self.assertTrue(Post.objects.exists())
