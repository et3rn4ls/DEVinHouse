import json
import os


filedb = os.path.join('./', 'data', 'pessoasdb.json')
pessoas = {"pessoas": []}


class Pessoa:

    def __init__(self, nome: str, celular: int, email: str):
        self.nome = nome
        self.celular = celular
        self.email = email
    
    @staticmethod
    def cadastrar_pessoa():
        nome = input('Nome: ')
        celular = int(input('Celular: '))
        email = input('E-mail: ')

        p = Pessoa(nome, celular, email)
        p.__salvar_pessoa()

    @staticmethod
    def exibir_pessoa():
        try:
            with open(filedb) as pessoadb:
                print(json.load(pessoadb))
        except FileNotFoundError as exception:
            print('\nNenhum cadastrado de pessoa localizado.')

    def __salvar_pessoa(self):
        print('\nSalvando ...')
        keys = ["nome", "celular", "email"]
        values = [self.nome, self.celular, self.email]
        pessoa = dict(zip(keys, values))
        pessoas['pessoas'].append(pessoa)

        try:
            with open(filedb, 'r+') as pessoadb:
                listaPessoas = json.load(pessoadb)
                listaPessoas['pessoas'].append(pessoa)
                pessoadb.seek(0)
                json.dump(listaPessoas, pessoadb)
        except FileNotFoundError as exception:
            with open(filedb, 'w') as pessoadb:
                json.dump(pessoas, pessoadb)
            self.__salvar_pessoa

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
        
