import json

class Endereco:

    def __init__(self, logradouro: str, numero: int, complemento: str, bairro: str, cidade: str, uf: str):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
    
    def cadastrar_endereco():
        logradouro = input('Logradouro: ')
        numero = int(input('Numero: '))
        complemento = input('Complemento: ')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        uf = input('UF: ')

        e = Endereco(logradouro, numero, complemento, bairro, cidade, uf)
        e.__salvar_endereco()

    def exibir_endereco():
        a_file = open('./data/enderecos.json', 'r')
        a_json = json.load(a_file)
        pretty_json = json.dumps(a_json, indent=4)
        a_file.close()
        print(pretty_json)

    def __salvar_endereco(self):
        print('Salvando...')
        keys = ["logradouro", "numero", "complemento", "bairro", "cidade", "uf"]
        values = [self.logradouro, self.numero, self.complemento, self.bairro, self.cidade, self.uf]
        endereco = dict(zip(keys, values))

        with open('./data/enderecos.json', 'w') as convert_file:
            convert_file.write(json.dumps(endereco))

        print('Endereço salvo!')

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
        