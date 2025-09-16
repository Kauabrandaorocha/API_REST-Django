# 📦 Projeto API de Endereços com Consulta via CEP (ViaCEP)

> **Desenvolvido como parte do Projeto Workshop Backend da Fábrica de Software - UNIPÊ 2025.2**

---

## 📌 Descrição

Esta aplicação backend permite o cadastro de endereços a partir de um **CEP** informado pelo usuário.  
Ao cadastrar um novo registro, a aplicação consulta automaticamente os dados completos do endereço na **API pública ViaCEP**, preenchendo os campos restantes (logradouro, bairro, localidade e UF).

---

## 🎯 Objetivos do Projeto

- ✅ Praticar o consumo de APIs externas com `requests`
- ✅ Utilizar `ModelViewSet` do Django REST Framework para construir uma API RESTful
- ✅ Implementar serialização e salvamento de dados dinâmicos
- ✅ Explorar o modelo MVT com Django
- ✅ Criar endpoints reutilizáveis com `router`

---

## 🧪 Funcionalidades

| Funcionalidade         | Descrição                                                       |
|------------------------|-----------------------------------------------------------------|
| `Cadastrar Endereço`   | Usuário informa o CEP, e os demais campos são preenchidos via API |
| `Listar Endereços`     | Exibe todos os endereços cadastrados no banco                   |
| `Visualizar Detalhes`  | Mostra informações completas de um endereço                     |
| `Atualizar Endereço`   | Permite editar um registro existente                            |
| `Excluir Endereço`     | Remove um registro da base de dados                             |

---

## 🌐 Sobre a API Utilizada

A integração é feita com a [ViaCEP API](https://viacep.com.br/), que retorna os dados do endereço no seguinte formato:

### Exemplo de retorno:

```json
{
  "cep": "58075500",
  "logradouro": "Rua Exemplo",
  "bairro": "Bairro Exemplo",
  "localidade": "João Pessoa",
  "uf": "PB"
}
```
## 🛠️ Tecnologias Utilizadas

- 🧩 Backend

- Python 3.10+

- Django 5.2

- Django REST Framework

- Requests (para consumo da API ViaCEP)

- SQLite3 (banco de dados padrão do Django)

## 🎨 Frontend

- Interface de administração Django (`/admin`)

- Endpoints da API acessíveis via navegador ou ferramentas como Postman, Insomnia, etc.

## 🧰 Requisitos de Instalação

Antes de rodar o projeto, você precisa ter:

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/)

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual:

Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

### 4. Baixe o django, o django rest framework(DRF) e os Requests:

```bash
pip install django djangorestframework requests
```

### 5. Crie um arquivo requirements.txt, contendo todas as dependências:

```bash
pip freeze > requirements.txt
```

- ### Se as dependências não forem instaladas, baixe-as com o seguinte código:

```bash
pip install -r requirements.txt
```

###  6. Crie o projeto Django (se ainda não criou):

```bash
django-admin startproject endereco_api
cd endereco_api
```

### 7. Crie o app Django:

```bash
python manage.py startapp enderecos
```

### 8. Adicione o app em settings.py:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'enderecos',
]
```

### 9. Configure os modelos no models.py:

```python
class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    localidade = models.CharField(max_length=100, blank=True)
    uf = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return f"{self.logradouro}, {self.bairro} - {self.localidade}/{self.uf}"
```

### 10. Configure as views, serializers e urls usando ModelViewSet + router

## 🧱 Migrações e Execução

### 11. Aplique as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 12. Crie um superusuário (opcional):

```bash
python manage.py createsuperuser
```

### 13. Rode o servidor:

```bash
python manage.py runserver
```

### 14. Acesse no navegador:

API: `http://127.0.0.1:8000/enderecos/`

Admin: `http://127.0.0.1:8000/admin/`

## 🔄 Endpoints esperados

| Método | Endpoint           | Ação                     |
| ------ | ------------------ | ------------------------ |
| GET    | `/enderecos/`      | Lista todos os endereços |
| POST   | `/enderecos/`      | Cria um novo endereço    |
| GET    | `/enderecos/<id>/` | Detalhes de um endereço  |
| PUT    | `/enderecos/<id>/` | Atualiza um endereço     |
| DELETE | `/enderecos/<id>/` | Exclui um endereço       |

## 📚 Fontes e Referências

### Durante o desenvolvimento do projeto, foram consultadas as seguintes documentações e materiais de apoio:

- Documentação Oficial do Django
👉 https://docs.djangoproject.com/pt-br/4.2/

- Django REST Framework (DRF)
👉 https://www.django-rest-framework.org/

- ViaCEP API (consulta de CEPs)
👉 https://viacep.com.br/

- Requests - Biblioteca HTTP para Python
👉 https://requests.readthedocs.io/

- MDN Web Docs - HTML, CSS, HTTP e Web APIs
👉 https://developer.mozilla.org/pt-BR/

- YouTube – Tutoriais diversos sobre Django, APIs e Python
👉 https://www.youtube.com/

- Dev.to – Artigos da comunidade de desenvolvedores
👉 https://dev.to/
