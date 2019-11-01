from django.test import TestCase
from django.urls import reverse
from .forms import PostForm
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('post_list'))

    def test_get(self):
        """Deve retornar código de estado 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Verificando se a template usada é a blog/post_list.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_list.html')


class PostListAuthorTest(TestCase):
    def setUp(self):
        user = User(email='nickb@wnj.com', username='test')
        user.set_password('N%sd00_pTs')
        user.save()
        self.resp = self.client.get(
            reverse('post_list_by_author', kwargs={'author_': user.username})
        )

    def test_get(self):
        """Deve retornar código de estado 200"""
        self.assertEqual(self.resp.status_code, 200)
    '''
    def test_template(self):
        """Verificando se a template usada é a blog/post_list.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_list.html')
    '''


class PostDetailTest(TestCase):
    def setUp(self):
        user = User(email='nickb@wnj.com', username='test')
        user.set_password('N%sd00_pTs')
        user.save()
        post = Post(
            title='Teste01',
            subtitle='Testando 01',
            text='texto texto',
            author=user)
        post.save()
        self.resp = self.client.get(
            reverse('post_detail', kwargs={'pk': post.pk}))

    def test_get(self):
        """Deve retornar código de estado 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Verificando se a template usada é a blog/post_list.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_detail.html')


class PostAddTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/post/new/')

    def test_get(self):
        """Deve retornar código de estado 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Verificando se a template usada é a blog/post_list.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_edit.html')

    def test_add_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, PostForm)
