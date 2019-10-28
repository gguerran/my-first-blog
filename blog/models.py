from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    '''
        Classe que define a entidade de Posts
        Atributos:
            author (fk_User): autor da postagem
            title (str): Título da postagem
            subtitle (str): Subtítulo da postagem
            text (str): Texto da postagem
            created_date (dataTime): Data que a postagem foi criada
            published_date (dataTime): Data em que a postagem foi publicada
        Métodos:
            publish: Define a data de pubicação na hora em que o método for
                chamado
            __str__: Define que, ao ser convertido em string, retorne o título
                do post
    '''
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=200)
    subtitle = models.CharField('Subtítulo', max_length=300, default='')
    text = models.TextField('Texto')
    created_date = models.DateTimeField(
        'Data de criação', default=timezone.now)
    published_date = models.DateTimeField(
        'Data de publicação', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
