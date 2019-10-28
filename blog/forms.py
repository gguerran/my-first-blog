from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    '''
    Classe para o formulário, que herda os campos do Model Post.
    Finalidade de gerar os formulários de adição e edição de Post's
    '''
    class Meta:
        '''
        Classe que define o Model que será 'formularizado'
        e os campos do mesmo.
        '''
        model = Post
        fields = ('title', 'subtitle', 'text',)
