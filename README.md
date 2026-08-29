# Projeto Fábrica de Software

Sistema de gerenciamento de produtos e categorias desenvolvido com Django.

## 📋 Descrição

Este projeto é uma aplicação Django para gerenciar um catálogo de produtos organizados por categorias. Inclui funcionalidades de criação, leitura, atualização e exclusão de produtos e suas respectivas categorias.

## 🎯 Funcionalidades

- **Gerenciamento de Categorias**: Criar, visualizar, editar e deletar categorias de produtos
- **Gerenciamento de Produtos**: Gerenciar produtos com informações de:
  - Nome do produto
  - Preço unitário
  - Quantidade em estoque
  - Categoria associada
- **Painel Administrativo**: Interface Django Admin para gerenciamento dos dados

## 🛠️ Tecnologias

- **Python** 3.x
- **Django** 5.2.17
- **SQLite** (banco de dados padrão)

## 📦 Instalação

### Pré-requisitos

- Python 3.x instalado
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. Clone ou baixe o projeto:
```bash
cd ProjetoFabricadesoftware
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
   - **Windows**:
   ```bash
   venv\Scripts\activate
   ```
   - **Linux/macOS**:
   ```bash
   source venv/bin/activate
   ```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute as migrações do banco de dados:
```bash
python manage.py migrate
```

6. Crie um superusuário para acessar o admin:
```bash
python manage.py createsuperuser
```

7. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

O aplicativo estará disponível em `http://127.0.0.1:8000/`

## 👨‍💼 Acesso ao Painel Admin

Para acessar o painel administrativo:

1. Acesse `http://127.0.0.1:8000/admin/`
2. Faça login com as credenciais do superusuário criado

## 📁 Estrutura do Projeto

```
projeto/
├── core/                    # App principal
│   ├── models.py           # Modelos (Categoria, Produto)
│   ├── admin.py            # Configuração do Django Admin
│   ├── views.py            # Visualizações
│   ├── urls.py             # URLs da app
│   ├── migrations/         # Migrações do banco de dados
│   └── ...
├── projeto/                # Configurações do projeto
│   ├── settings.py         # Configurações Django
│   ├── urls.py             # URLs principais
│   ├── wsgi.py             # WSGI para produção
│   └── asgi.py             # ASGI para aplicações assíncronas
├── manage.py               # Script de gerenciamento Django
├── db.sqlite3              # Banco de dados SQLite
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
```

## 🗄️ Modelos de Dados

### Categoria
- `id`: Identificador único (auto-incrementado)
- `nome`: Nome da categoria (máx. 100 caracteres)

### Produto
- `id`: Identificador único (auto-incrementado)
- `nome`: Nome do produto (máx. 100 caracteres)
- `preco`: Preço unitário (até 10 dígitos, 2 casas decimais)
- `estoque`: Quantidade em estoque (número inteiro)
- `categoria`: Relacionamento com Categoria (Chave estrangeira)

## 🔧 Comandos Úteis

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Iniciar servidor de desenvolvimento
python manage.py runserver

# Criar novo app
python manage.py startapp nome_app

# Shell Django (console interativo)
python manage.py shell
```

## 📝 Notas de Desenvolvimento

- O arquivo `db.sqlite3` é gerado automaticamente. Adicione-o ao `.gitignore`
- As variáveis sensíveis (como `SECRET_KEY`) devem ser movidas para variáveis de ambiente em produção
- Configure `ALLOWED_HOSTS` apropriadamente para produção

## 📧 Contato

Para dúvidas ou sugestões sobre o projeto, entre em contato.

---

**Última atualização**: 2026-08-29
