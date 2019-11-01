from django.test import TestCase
# Create your tests here.


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """Deve retornar código de estado 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Verificando se a template usada é a blog/post_list.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_list.html')


class PostListAuthorTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/post/author/admin/')

    def test_get(self):
        """Deve retornar código de estado 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Verificando se a template usada é a blog/post_list.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_list.html')
