from django.test import TestCase
from django.urls import reverse
from .forms import PostForm
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.


class PostListTest(TestCase):

    def setUp(self):
        user = User(email='gustavo@gmail.com',
                    username='test', password='N%sd00_pTs')
        user.save()

        post = Post(
            title='Teste01',
            subtitle='Testando 01',
            text='texto texto',
            author=user)
        post.save()

        post2 = Post(
            title='Teste01',
            subtitle='Testando 01',
            text='texto texto',
            author=user)
        post2.save()

        self.resp = self.client.get(reverse('post_list'))

    def test_get(self):
        """Deve retornar código de estado 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Deve verificar se a template usada é a blog/post_list.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_list.html')


class PostListByAuthorTest(TestCase):
    def setUp(self):
        user = User(email='gustavo@gmail.com',
                    username='test', password='N%sd00_pTs')
        user.save()

        self.resp = self.client.get(
            reverse('post_list_by_author', kwargs={'author_': user.username})
        )

    def test_get(self):
        """Deve retornar código de estado 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Deve verificar se a template usada é a blog/post_list.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_list.html')


class PostDetailTest(TestCase):
    def setUp(self):
        user = User(email='gustavo@gmail.com',
                    username='test', password='N%sd00_pTs')
        user.save()

        post = Post(
            title='Teste01',
            subtitle='Testando 01',
            text='texto texto',
            author=user)
        post.save()

        self.resp = self.client.get(
            reverse('post_detail', kwargs={'pk': post.pk}))

    def test_status_code(self):
        """Deve retornar código de estado 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Deve verificar se a template usada é a blog/post_detail.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_detail.html')


class PostAddTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('post_new'))

    def test_status_code(self):
        """Deve retornar código de estado 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Deve verificar se a template usada é a blog/post_edit.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_edit.html')

    def test_add_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, PostForm)


class PostEditTest(TestCase):
    def setUp(self):
        user = User(email='gustavo@gmail.com',
                    username='test', password='N%sd00_pTs')
        user.save()

        post = Post(
            title='Teste01', subtitle='Testando 01', text='texto texto',
            author=user)
        post.save()

        self.resp = self.client.get(
            reverse('post_edit', kwargs={'pk': post.pk}))

    def test_status_code(self):
        """Deve retornar código de estado 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Deve verificar se a template usada é a blog/post_edit.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_edit.html')

    def test_add_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, PostForm)


class PostDeleteTest(TestCase):
    def setUp(self):
        user = User(email='gustavo@gmail.com',
                    username='test', password='N%sd00_pTs')
        user.save()

        post = Post(
            title='Teste01', subtitle='Testando 01', text='texto texto',
            author=user)
        post.save()

        self.resp = self.client.get(
            reverse('post_delete', kwargs={'pk': post.pk}))

    def test_status_code(self):
        """Deve retornar código de estado 302, redirecionando a página"""
        self.assertEqual(self.resp.status_code, 302)
