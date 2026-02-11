import os
import json
from datetime import datetime, date

arquivo_dados = 'dados.json'
arquivo_log = 'log.txt'

def logEntrada():
    if not os.path.exists('LogEntrada.txt'):
        with open('LogEntrada.txt', 'w', encoding='utf-8') as log:
            log.write('\n---CADASTRO DE USUARIOS---\n')

def carregar_dados():
    if not os.path.exists(arquivo_dados):
        return []
    try:
        with open(arquivo_dados, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        return []

def salvar_dados(usuarios):
    with open(arquivo_dados, 'w', encoding='utf-8') as arq:
        json.dump(usuarios, arq, indent=4, ensure_ascii=False)

def contaExiste(nome, usuarios):
    for u in usuarios:
        if u['usuario'] == nome:
            return True
    return False

def repetir_senha():
    while True:
        senha = input('Digite a senha: ')
        repSenha = input('Repita a senha: ')

        if senha != repSenha:
            print('As senha não são iguais, tente novamente')
            continue
        return senha

def pedir_usuario(usuarios):
    while True:
        usuario = input('Digite o usuario: ')
        if contaExiste(usuario, usuarios):
            print('Esse usuário ja existe, Tente novamente!!')
            continue
        return usuario

def salvar_conta(usuarios, usuario, senha):
        usuarios.append({
            'usuario': usuario, 
            'senha': senha
            })
            
        salvar_dados(usuarios)
        print('Registro concluído!!')
        pausar()


def registrar_dados(usuarios):
    
    while True:
        usuario = pedir_usuario(usuarios)
        senha = repetir_senha()
        salvar_conta(usuarios, usuario, senha)

def informações_conta():
    with open('LogEntrada.txt', 'r', encoding='utf-8') as log:
        leia = log.readlines()

        if leia:
            ultima_leia = leia[-1].strip()
            print('---INFORMAÇÕES DA CONTA---')
            print(ultima_leia)
            pausar()

def pedir_usuario_confirmar(usuarios):
   
    while True:
        confi_usuario = input('Confirme seu usuário: ')
        for usuario in usuarios:
            if usuario['usuario'] == confi_usuario:
                return usuario
        print('Usuário não encontrado!!')
            
def verificar_senha(usuario, tentativa=5):
    while tentativa > 0:
        senha_atual = input("Digite sua senha atual: ")
        rep_senha = input("Repita a senha: ")
        if senha_atual != rep_senha:
            tentativa -= 1
            print("As senhas não são iguais, tente novamente")
            continue
        if usuario ['senha'] == senha_atual:
            return True
        else:
            tentativa -= 1
            print(f"Senha incorreta! Restam {tentativa} tentativas")
    return False 

def pausar():
    input("Pressione ENTER para continuar")

def pedir_nova_senha():
    while True:
        nova_senha = input('Digite a nova senha: ')
        rep_senha_nova = input('Digite a nova senha novamente: ')

        if nova_senha != rep_senha_nova:
            print('As senhas não são iguais! tente novamente!')
            continue
        return nova_senha
    
def mudar_senha(usuarios):
    
    print('\n---MENU SENHA---')

    usuario_atual = pedir_usuario_confirmar(usuarios)

    if not verificar_senha(usuario_atual):
        print("Não foi possível alterar a senha, retornando para o menu")
        return
    nova_senha = pedir_nova_senha()
    usuario_atual['senha'] = nova_senha
    salvar_dados(usuarios)
    print("Senha alterada com sucesso!!")
    pausar()

def menu_pos_login():
    while True:
        print('-=-'*20)
        print('[1]-ALTERAR SENHA')
        print('[2]-INFORMAÇÕES DA CONTA')
        print('[3]-DELETAR CONTA')
        print('[4]-LOGOUT')
        resposta = input('Digite a opção que deseja: ')

        if resposta == "1":
            mudar_senha()
        elif resposta == "2":
            informações_conta()
        elif resposta == "3":
            deletar_conta()
        elif resposta == "4":
            print('Obrigado por usar nossos serviços!!')
            dataLog = date.today()
            horaLog = datetime.now().strftime('%H:%M:%S')

            with open('LogEntrada.txt', 'a', encoding='utf-8') as regLL:
                regLL.write(f'LogOut - {dataLog} - {horaLog}\n')
 
                 
def login_dados():
    usuarios = carregar_dados()
    
    usuario_digitado = input('Digite seu usuário: ')
    senha_digitado = input('Digite sua senha: ')
    
    login_valido = False
    for u in usuarios:
        if u["usuario"] == usuario_digitado:
            if u["senha"] == senha_digitado:
                login_valido = True
                break
    if login_valido:
        print('Login concluído!')
        dataLog = date.today()
        horaLog = datetime.now().strftime('%H:%M:%S')

        with open('LogEntrada.txt', 'a', encoding='utf-8') as regLL:
            regLL.write(f'{usuario_digitado} Log - {dataLog} - {horaLog}\n')
        logEntrada()
        menu_pos_login()
    else:
        print('Informações incorretas')

def verificar_senha_simples(usuario):
    senha_digitada = input("Digite sua senha atual: ")
    if usuario['senha'] == senha_digitada:
        return True
    else:
        print("Senha incorreta")
        return False

def deletar_conta():
    usuarios = carregar_dados()

    print("---DELETAR CONTA---\n")
          
    usuario_atual = pedir_usuario_confirmar(usuarios)

    if not verificar_senha_simples(usuario_atual):
        print("Não foi possível deletar a conta, retornando ao ao menu.")
        pausar()
        return

    usuarios.remove(usuario_atual)
    salvar_dados(usuarios)
    print(f"usuário {usuario_atual['usuario']} deletado com sucesso!")
    pausar()

def menu():
    while True:
        print('-=-'*20)
        print('[1]-REGISTRAR CONTA')
        print('[2]-LOGAR CONTA')
        print('[3]-SAIR')

        resposta = input('Digite a opção selecionada: ')

        if resposta == '1':
            print('\n---MENU DE REGISTRO---\n')
            registrar_dados()
        elif resposta == '2':
            print('\n---MENU DE LOGIN---\n')
            login_dados()
        elif resposta == '3':
            print('Obrigado por usar nossos serviços!!')
            exit()
        else:
            print('Selecione uma opção válida!!')
            
menu()
