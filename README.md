# 🏭 Fábrica de Software - Backend Django

Projeto Django completo com CRUD de produtos e integração com API OpenLibrary.

## 📋 Funcionalidades

- ✅ **CRUD Completo** - Criar, Ler, Atualizar e Deletar produtos
- ✅ **Categorias** - Produtos organizados por categorias (Eletrônicos, Roupas, Alimentos)
- ✅ **API OpenLibrary** - Buscar livros em tempo real
- ✅ **Banco de Dados SQLite** - Persistência de dados com 15 produtos pré-carregados
- ✅ **Interface Responsiva** - HTML + CSS moderno com design gradient

## 🚀 Como Executar

### 1. Clonar o repositório
```bash
git clone https://github.com/HeitorcDEV/wsBackendFabricaDeSoftware26.2.git
cd wsBackendFabricaDeSoftware26.2
```

### 2. Criar e ativar ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows

source venv/bin/activate  # Linux/macOS
```
### Se der erro use 
```bash
Set-ExecutionPolicy -Scope Process Bypass
```
### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Executar migrações (se necessário)
```bash
python manage.py migrate
```

### 5. Iniciar servidor
```bash
python manage.py runserver
```

Acesse:
- **Lista de Produtos**: http://127.0.0.1:8000/produtos/
- **Buscar Livros (API)**: http://127.0.0.1:8000/api/
- **Painel Admin**: http://127.0.0.1:8000/admin/

## 📁 Estrutura do Projeto

```
ProjetoFabricadesoftware/
├── projeto/                    # Configurações Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── core/                       # App principal
│   ├── models.py               # Modelos (Produto, Categoria)
│   ├── views.py                # Lógica das views (CRUD + API)
│   ├── urls.py                 # Rotas do app
│   ├── admin.py                # Configuração Admin
│   ├── templates/              # Templates HTML
│   │   ├── read.html           # Listar produtos
│   │   ├── create.html         # Criar produto
│   │   ├── update.html         # Editar produto
│   │   ├── delete.html         # Deletar produto
│   │   └── vizualizarAPI.html  # Buscar livros
│   └── migrations/
├── manage.py
├── db.sqlite3                  # Banco de dados (com dados pré-carregados)
├── requirements.txt            # Dependências
├── .gitignore
└── README.md
```

## 🔧 Tecnologias

- **Backend**: Django 5.2.17
- **Banco de Dados**: SQLite3
- **API Externa**: OpenLibrary (https://openlibrary.org/search.json)
- **HTTP Client**: Requests
- **Python**: 3.10+

## 📊 Modelos de Dados

### Categoria
```python
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
```

**Categorias pré-carregadas:**
- Eletrônicos
- Roupas
- Alimentos

### Produto
```python
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
```

**Dados de Exemplo (15 produtos):**
- iPhone 15, Samsung S24, Fone Sony, Notebook Lenovo, Monitor LG, Teclado Mecânico
- Camiseta Nike, Calça Adidas, Tênis Puma, Jaqueta Impermeável, Meias Puket
- Arroz 5kg, Feijão 2kg, Óleo 1l, Açúcar 2kg

## 🌐 Rotas da Aplicação

| Método | URL | Descrição |
|--------|-----|-----------|
| GET | `/` | Redireciona para lista de produtos |
| GET | `/produtos/` | Lista todos os produtos |
| GET/POST | `/produtos/criar/` | Formulário e criação de produto |
| GET/POST | `/produtos/<id>/editar/` | Formulário e edição de produto |
| POST | `/produtos/<id>/deletar/` | Página de confirmação e deleção |
| GET | `/api/` | Buscar livros na OpenLibrary API |
| GET | `/admin/` | Painel administrativo Django |

## 🔍 Como Usar o CRUD

### Criar Produto
1. Clique em "+ Novo" na página de produtos
2. Preencha os campos (nome, preço, estoque, categoria)
3. Clique em "Salvar"

### Editar Produto
1. Clique em "Editar" no produto desejado
2. Modifique os valores
3. Clique em "Atualizar"

### Deletar Produto
1. Clique em "Deletar" no produto desejado
2. Confirme a ação na página de confirmação

### Buscar Livros
1. Acesse `/api/`
2. Digite o nome de um livro ou autor
3. Visualize os resultados com detalhes (título, autor, ano, edições, ISBN)

## 📚 Consumindo a API OpenLibrary

A rota `/api/` consome dados da API OpenLibrary:
```
GET https://openlibrary.org/search.json?q=python
```

Exemplo de resposta:
```json
{
  "docs": [
    {
      "title": "Learning Python",
      "author_name": ["Mark Lutz"],
      "first_publish_year": 1996,
      "edition_count": 42,
      "isbn": ["0596513984"],
      "language": ["en"]
    }
  ]
}
```

## 🔧 Comandos Úteis

```bash
# Criar migrações baseadas em models.py
python manage.py makemigrations

# Aplicar migrações ao banco de dados
python manage.py migrate

# Criar superusuário para admin
python manage.py createsuperuser

# Iniciar servidor de desenvolvimento
python manage.py runserver

# Acessar console Python com Django pré-carregado
python manage.py shell
```

## 💾 Banco de Dados

O projeto usa SQLite3 com o arquivo `db.sqlite3` que:
- ✅ Já está pré-carregado com 3 categorias e 15 produtos
- ✅ É versionado no Git (para fins de demonstração)
- ✅ Pode ser resetado executando `python manage.py migrate`

## 📦 Dependências

Veja [requirements.txt](requirements.txt) para a lista completa. Principais:
- Django==5.2.17
- requests==2.32.3
- sqlparse==0.6.0
- asgiref==3.12.1

## 🎨 Design

- Interface limpa e moderna com gradientes
- Layout responsivo (mobile-friendly)
- Cores: Roxo (#667eea) e Violeta (#764ba2)
- Ícones e emojis para melhor UX

## 👨‍💻 Autor

**Heitor C. DEV**
- GitHub: [@HeitorcDEV](https://github.com/HeitorcDEV)
- Projeto: wsBackendFabricaDeSoftware26.2

## 📝 Licença

MIT License - Sinta-se livre para usar este projeto

---
**Criado em**: Agosto de 2026
**Versão**: 1.0

**Última atualização**: 2026-08-29
