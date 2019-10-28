from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import User


def post_list(request):
    """
    Função que renderiza a página inicial (que lista todos os posts do blog)
    """
    # Variável que indica a template que vai ser renderizada
    template_name = 'blog/post_list.html'
    # Variável que armazena a lista de todos os Post's salvos no banco de dados
    # realizando um filtro de objetos que foram postados até o momento,
    # ordenando por data de publicação
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    # Variável que define o contexto que a página vai ser renderizada
    # (nesse caso todos os posts publicados)
    context = {'posts': posts}
    # Retorna a renderização da template com contexto indicado
    return render(request, template_name, context)


def post_list_by_author(request, author_):
    """
    Função que renderiza a página que lista todos os posts de um autor.
    """
    # Variável que indica a template que vai ser renderizada
    template_name = 'blog/post_list.html'
    # Variável que busca o autor, passado como parâmetro para a função
    _author = get_object_or_404(User, username=author_)
    # Variável que armazena a lista de todos os Post's salvos no banco de dados
    # realizando um filtro de objetos que foram postados até o momento pelo
    # autor, ordenando por data de publicação
    posts = Post.objects.filter(
        author=_author, published_date__lte=timezone.now()
    ).order_by('published_date')
    # Variável que define o contexto que a página vai ser renderizada
    # (nesse caso todos os posts publicados por determinado autor)
    context = {'posts': posts}
    # Retorna a renderização da template com contexto indicado
    return render(request, template_name, context)


def post_detail(request, pk):
    """
    Função que renderiza a página que detalha o post selecionado.
    """
    # Variável que indica a template que vai ser renderizada
    template_name = 'blog/post_detail.html'
    # Variável que busca o post, que a pk (primayr key)
    # passada como parâmetro para a função
    post = get_object_or_404(Post, pk=pk)
    # Variável que define o contexto que a página vai ser renderizada
    # (nesse caso todos o post selecionado)
    context = {'post': post}
    # Retorna a renderização da template com contexto indicado
    return render(request, template_name, context)


def post_new(request):
    """
    Função que renderiza a página cria um novo post.
    """
    # Variável que indica a template que vai ser renderizada
    template_name = 'blog/post_edit.html'
    # Verificação se na requisição exite algum POST

    acao = 'Adicionar'
    if request.method == "POST":
        # O form que veio da requisição POST é convertido no modelForm
        form = PostForm(request.POST)
        # Se for válido
        if form.is_valid():
            # O post armazena os dados do formulário
            post = form.save(commit=False)
            # Configura como autor, o usuário ativo
            post.author = request.user
            # Configura a data de publicação para o momento de criação
            post.published_date = timezone.now()
            # Salva o post criado
            post.save()
            # Redireciona para a visualização do post recém criado
            return redirect('post_detail', pk=post.pk)
    else:
        # Caso não tenha, o formulário é criado para ser renderizado
        form = PostForm()
        # Variável que define o contexto que a página vai ser renderizada
        # (nesse caso o formulário selecionado)
        context = {'form': form, 'acao': acao}
        # Retorna a renderização da template com contexto indicado
        return render(request, template_name, context)


def post_edit(request, pk):
    # Variável que indica a template que vai ser renderizada
    template_name = 'blog/post_edit.html'
    # Variável que busca o post que foi selecionado

    acao = 'Editar'
    post = get_object_or_404(Post, pk=pk)
    # Se tiver alguma coisa no POST da requisição
    if request.method == "POST":
        # O form que veio da requisição POST é convertido no modelForm com os
        # dados já existentes no banco
        form = PostForm(request.POST, instance=post)
        # Se for válido
        if form.is_valid():
            # O post armazena os dados do formulário
            post = form.save(commit=False)
            # Configura como autor, o usuário ativo
            post.author = request.user
            # Atera a data de publicação para o momento da alteração
            post.published_date = timezone.now()
            # Salva o post editado
            post.save()
            # Redireciona para a visualização do post recém editado
            return redirect('post_detail', pk=post.pk)
    else:
        # Caso não tenha, o formulário é criado para ser renderizado já com os
        # dados do objeto a ser editado
        form = PostForm(instance=post)
        # Variável que define o contexto que a página vai ser renderizada
        # (nesse caso o formulário selecionado)
        context = {'form': form, 'acao': acao}
        # Retorna a renderização da template com contexto indicado
        return render(request, template_name, context)


def post_delete(request, pk):
    # Variável que busca o post que foi selecionado
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
