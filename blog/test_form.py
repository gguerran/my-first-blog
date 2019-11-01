from django.test import TestCase
from .forms import PostForm


class PostFormTest(TestCase):
    def setUp(self):
        self.form = PostForm()

    def test_form_has_fields(self):
        """Form deve ter os campos 'title', 'subtitle' e 'text'."""
        expected = ['title', 'subtitle', 'text']
        self.assertSequenceEqual(expected, list(self.form.fields))
