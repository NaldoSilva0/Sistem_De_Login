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

def registrar_dados():
    usuarios = carregar_dados()

    while True:
        usuario = input('Digite o usuario: ').lower()
        if contaExiste(usuario, usuarios):
            print('Esse usuário ja existe, Tente novamente!!')
            continue

        senha = input('Digite a senha: ')
        repSenha = input('Repita a senha: ')

        if senha != repSenha:
            print('As senha não são iguais, tente novamente')
            continue

        usuarios.append({
            'usuario': usuario, 
            'senha': senha
            })
        
        salvar_dados(usuarios)
        print('Registro concluído!!')
        break
    menu()

def informações_conta():
    with open('LogEntrada.txt', 'r', encoding='utf-8') as log:
        leia = log.readlines()

        if leia:
            ultima_leia = leia[-1].strip()
            print('---INFORMAÇÕES DA CONTA---')
            print(ultima_leia)
            input('Aperte ENTER para voltar ao menu')

def mudar_senha():
    usuarios = carregar_dados()
    contador = 5
    
    print('\n---MENU SENHA---')

    encontrado = False
    while not encontrado:
        confi_usuario = input('Confirme seu usuário: ')
        for usuario in usuarios:
            if usuario['usuario'] == confi_usuario:
                encontrado = True
                usuario_atual = usuario
                break
        if not encontrado:
            print('Usuário não encontrado!!')

    while contador > 0:
        contador -= 1
        senha_atual = input('Digite a senha atual: ')
        rep_senha_atual = input('Digite a senha novamente: ')
        if senha_atual != rep_senha_atual:
            print(f'As senhas não são iguais, restam {contador} tentativas')
            senha_atual = input('Digite a senha atual: ')
            rep_senha_atual = input('Digite a senha novamente: ')
        else:

            while True:
                nova_senha = input('Digite a nova senha: ')
                rep_senha_nova = input('Digite a nova senha novamente: ')

                if nova_senha != rep_senha_nova:
                    print('As senhas não são iguais! tente novamente!')
                    continue

                if usuario_atual['senha'] != senha_atual:
                    print('Senha atual incorreta! tente novamente')
                    break

                usuario_atual['senha'] = nova_senha

                with open(arquivo_dados, 'w', encoding='utf-8') as arq:
                    json.dump(usuarios, arq, indent=4, ensure_ascii=False)

                print('Senha atual alterada!')
                
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
            menu()
                 
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
       
def deletar_conta():
    indice_encontrado = None
    usuarios = carregar_dados()

    usuario_excluir = input('Digite o usuário: ')
    senha_excluir = input('Digite a senha: ')

    for i, usuario in enumerate(usuarios):

        if usuario["usuario"] == usuario_excluir:
            if usuario["senha"] == senha_excluir:
                indice_encontrado = i
                break
    if indice_encontrado == None:
        print('Usuário não encontrado!!')
    else:
        del usuarios[indice_encontrado]
        print('Usuário deleteado!!')
    with open(arquivo_dados, 'w', encoding='utf-8') as arq:
        json.dump(usuarios, arq, indent=4, ensure_ascii=False)
        exit()

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