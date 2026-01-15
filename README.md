# Sistema de Cadastro e Login em Python

Este projeto é um **sistema simples de gerenciamento de usuários** feito em Python, utilizando **JSON** para armazenamento de dados. Ele permite que o usuário:

- Crie contas com validação de duplicidade
- Faça login
- Altere sua senha
- Exclua sua conta
- Navegue em um menu pós-login personalizado

---

## Funcionalidades

### Menu Principal
1. **Registrar conta**: cria um novo usuário com senha.
2. **Logar conta**: acessa o menu interno do usuário após autenticação.
3. **Sair**: encerra o programa.

### Menu Pós-Login
1. **Alterar senha**: permite ao usuário atualizar sua senha.
2. **Excluir conta**: remove a conta do usuário após confirmação de senha.
3. **Sair do menu**: retorna ao menu principal.

---

## Estrutura dos Dados

Os usuários são armazenados em um arquivo `dados.json` como uma lista de dicionários:

```json
[
    {
        "usuario": "exemplo",
        "senha": "1234"
    },
    {
        "usuario": "teste",
        "senha": "senha"
    }
]
