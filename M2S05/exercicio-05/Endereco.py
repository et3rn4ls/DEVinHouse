import json
import os
from os.path import exists


filedb = os.path.join('./', 'data', 'enderecodb.json')
enderecos = []


class Endereco:

    def __init__(self, logradouro: str, numero: int, complemento: str, bairro: str, cidade: str, uf: str):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
    
    @staticmethod
    def cadastrar_endereco():
        logradouro = input('Logradouro: ')
        numero = int(input('Numero: '))
        complemento = input('Complemento: ')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        uf = input('UF: ')

        e = Endereco(logradouro, numero, complemento, bairro, cidade, uf)
        e.__salvar_endereco()

    @staticmethod
    def exibir_endereco():
        with open(filedb) as enderecodb:
            print(json.load(enderecodb))

    def __salvar_endereco(self):
        print('\nSalvando...')
        keys = ["logradouro", "numero", "complemento", "bairro", "cidade", "uf"]
        values = [self.logradouro, self.numero, self.complemento, self.bairro, self.cidade, self.uf]
        endereco = dict(zip(keys, values))
        enderecos.append(endereco)

        if exists(filedb):
            with open(filedb) as enderecodb:
                listaEnderecos = json.load(enderecodb)
                listaEnderecos.append(endereco)
            with open(filedb, "w") as enderecodbrw:
                json.dump(listaEnderecos, enderecodbrw)
        else:
            with open(filedb, "w") as enderecodbrw:
                json.dump(enderecos, enderecodbrw)

        print('\nEndereço salvo!')


if __name__ == "__main__":

    while True:
        print("""
            Selecione uma opção:

            [1] Cadastrar endereço
            [2] Exibir endereço
            [0] Sair
        """)

        op = int(input('Opção: '))

        if op == 0:
            print ('Saindo ...')
            break

        if op == 1:
            Endereco.cadastrar_endereco()
        elif op == 2:
            Endereco.exibir_endereco()
        else:
            print('Opção inválida!')
        