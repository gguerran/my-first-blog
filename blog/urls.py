from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),

    path('login_redir/', views.login_redir, name='login_redir'),

    path('logout/', views.logout_view, name='logout_view'),

    path('pass_recovery/', views.pass_recovery, name='pass_recovery'),

    path('create_user/', views.create_user, name='create_user'),

    # Redireciona a página inicial para view post_list
    path('blog/', views.post_list, name='post_list'),
    # Redireciona para a view post_detail. Com a chave primária sendo passada
    # na url para a busca no banco de dados
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # Redireciona para a view post_list_by_author. Com o username do autor
    # sendo passado na url para a busca no banco de dados
    path('post/author/<str:author_>', views.post_list_by_author,
         name='post_list_by_author'),
    # Redireciona para a view post_new para a criação de um novo post
    path('post/new/', views.post_new, name='post_new'),
    # Redireciona para a view post_edit para a edição de um post já existente
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),


]
