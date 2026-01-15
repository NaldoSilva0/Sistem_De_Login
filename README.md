# Sistema de Cadastro e Login com Menu Pós-Login em Python

Este projeto é um **sistema completo de gerenciamento de usuários** feito em Python, utilizando **JSON** para armazenamento e **arquivo de log** para registrar atividades. O sistema permite:

- Registro de usuários com validação
- Login seguro
- Menu pós-login com opções avançadas
- Alteração de senha
- Consulta de informações da conta
- Exclusão de conta
- Registro de logs de login e logout

---

## Funcionalidades

### Menu Principal
1. **Registrar conta**: cria um novo usuário com senha.
2. **Logar conta**: autentica o usuário e abre o menu pós-login.
3. **Sair**: encerra o programa.

### Menu Pós-Login
1. **Alterar senha**: permite ao usuário atualizar sua senha atual.
2. **Informações da conta**: exibe o último registro no log da conta.
3. **Deletar conta**: remove a conta do usuário após confirmação de senha.
4. **Logout**: encerra a sessão do usuário e registra no log.

---

## Estrutura dos Arquivos

### `dados.json`
Armazena os usuários em formato JSON:

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
