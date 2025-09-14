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
