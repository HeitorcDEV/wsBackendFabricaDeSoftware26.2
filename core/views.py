from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria
import requests

def home(request):
    return redirect('listar_produtos')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'read.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == 'POST':
        Produto.objects.create(
            nome=request.POST['nome'],
            preco=request.POST['preco'],
            estoque=request.POST['estoque'],
            categoria_id=request.POST['categoria']
        )
        return redirect('listar_produtos')
    
    return render(request, 'create.html', {'categorias': Categoria.objects.all()})

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'POST':
        produto.nome = request.POST['nome']
        produto.preco = request.POST['preco']
        produto.estoque = request.POST['estoque']
        produto.categoria_id = request.POST['categoria']
        produto.save()
        return redirect('listar_produtos')
    
    return render(request, 'update.html', {'produto': produto, 'categorias': Categoria.objects.all()})

def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
    
    return render(request, 'delete.html', {'produto': produto})


def vizualizar_API(request):
    livros = []
    erro = None
    query = request.GET.get('q', '')
    
    try:
        response = requests.get(f'https://openlibrary.org/search.json?q={query}')
        if response.status_code == 200:
            dados = response.json()
            livros = dados.get('docs', [])[:10]
    except Exception as e:
        erro = f"Erro ao conectar: {str(e)}"
    
    return render(request, 'vizualizarAPI.html', {'livros': livros, 'erro': erro, 'query': query})
