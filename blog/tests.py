from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class HomeTest(TestCase):
    def setUp(self):
        url = reverse('post_list')
        self.resp = self.client.get(url)

    def test_get(self):
        """Deve retornar código de estado 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Verificando se a template usada é a blog/post_list.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_list.html')


class PostListAuthorTest(TestCase):
    def setUp(self):
        url = reverse('post_list_by_author', kwargs={'author_': 'admin'})
        self.resp = self.client.get(url)

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
        url = reverse('post_detail', kwargs={'pk': 3})
        self.resp = self.client.get(url)

    def test_get(self):
        """Deve retornar código de estado 200"""
        self.assertEqual(self.resp.status_code, 200)
    '''
    def test_template(self):
        """Verificando se a template usada é a blog/post_list.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_list.html')
    '''
