#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 08:56:11 2023

@author: caroline
"""

#Criando a classe para controle de usuários usando hash:

from hashlib import sha256 #importando algoritmo sha256 para utilização da hash no código

class Usuario():
    def __init__(self, nome, senha, nivel):
        self.login = nome
        self.passsword = self.hash_senha(senha)
        self.permission = nivel
        
    def hash_senha(self, senha): #transformação da senha em hash SHA256e retorno em hexadecimal
        hash_senha = sha256(senha.encode())
        return hash_senha.hexdigest()
        
    def verificacao_senha(self, senha):
        return self.passsword == self.hash_senha(senha)  
        
#Definindo informações de cadastro de usuários:

usuario1 = Usuario("usuario1", "1234", "adm")
usuario2 = Usuario("usuario2", "Abcd", "moderador")
#usuario3 = Usuario("João", "GHJ", "funcionário")
#usuario4 = Usuario("Mariana", "78910", "adm")
    
#Coletando dados para utilizar o controle de usuário criado:
    
nome_login = input("Digite seu nome: ")
senha_login = input("Digite sua senha: ")
    
usuario1.hash_senha(senha_login)
    
if usuario1.verificacao_senha(senha_login):
    print("Senha correta")
    print("\n")
    print(f"Sua permissão é de {usuario1.permission}")     
else:
    print("Senha incorreta. Tente novamente.")