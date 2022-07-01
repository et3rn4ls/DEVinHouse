import json
import os
from os.path import exists


filedb = os.path.join('./', 'data', 'pessoasdb.json')
pessoas = []


class Pessoa:

    def __init__(self, nome: str, celular: int, email: str):
        self.nome = nome
        self.celular = celular
        self.email = email
    
    def cadastrar_pessoa():
        nome = input('Nome: ')
        celular = int(input('Celular: '))
        email = input('E-mail: ')

        p = Pessoa(nome, celular, email)
        p.__salvar_pessoa()

    def exibir_pessoa():
        with open(filedb) as pessoadb:
            print(json.load(pessoadb))

    def __salvar_pessoa(self):
        print('\nSalvando ...')
        keys = ["nome", "celular", "email"]
        values = [self.nome, self.celular, self.email]
        pessoa = dict(zip(keys, values))
        pessoas.append(pessoa)

        if exists(filedb):
            with open(filedb) as pessoadb:
                listaPessoas = json.load(pessoadb)
                listaPessoas.append(pessoa)
            with open(filedb, "w") as pessoadbrw:
                json.dump(listaPessoas, pessoadbrw)
        else:
            with open(filedb, "w") as pessoadbrw:
                json.dump(pessoas, pessoadbrw)

        print('\Cadastro salvo!')


if __name__ == "__main__":

    while True:
        print("""
            Selecione uma opção:

            [1] Cadastrar pessoa
            [2] Exibir pessoas
            [0] Sair
        """)

        op = int(input('Opção: '))

        if op == 0:
            print ('Saindo ...')
            break

        if op == 1:
            Pessoa.cadastrar_pessoa()
        elif op == 2:
            Pessoa.exibir_pessoa()
        else:
            print('Opção inválida!')
        
