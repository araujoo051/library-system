from classes import Livro
from classes import Filial


class Livraria():
    def __init__ (self):
        self.filiais = []
        
    def cadastroLivros(self):  
        codigo = int(input("Codigo: "))
        titulo = input("Titulo: ")
        ano = int(input("Ano: "))
        area = input("Area: ")
        editora = input("Editora: ")
        valor = float(input("Valor: "))
        estoque = int(input("Estoque: "))
        numero_filial = int(input("Qual o número da filial?"))
        filial = next((f for f in self.filiais if f.numero == numero_filial), None)
        if filial is not None:
            livro = Livro(codigo, titulo, ano, area, editora, valor, estoque, filial)
            filial.adicionar_livro(livro)
            print("Livro cadastrado com sucesso!")
        else:
            print(f"Erro: Filial com número {numero_filial} não encontrada. Cadastro do livro cancelado.")

    def listarLivros (self):
        if not self.filiais:
            print("Nenhuma filial cadastrada.")
            return
        print("Filiais disponíveis:")
        for filial in self.filiais:
            print(f"{filial.nome} - {filial.numero}")
        try:
            numero_filial = int(input("Digite o número da filial: "))
        except ValueError:
            print("Número da filial inválido.")
            return
        filial = next((f for f in self.filiais if f.numero == numero_filial), None)
        if not filial:
            print("Filial não encontrada.")
            return
        
        print(f"\nLivros na Filial {filial.numero}:")
        for livro in filial.livros:
            print(livro)

    def buscarNome (self):
        if not self.filiais:
            print("Nenhuma filial cadastrada.")
            return
        print("Filiais disponíveis:")
        for filial in self.filiais:
            print(f"{filial.nome} - {filial.numero}")
        try:
            numero_filial = int(input("Digite o número da filial: "))
        except ValueError:
            print("Número da filial inválido.")
            return
        filial = next((f for f in self.filiais if f.numero == numero_filial), None)
        if not filial:
            print("Filial não encontrada.")
            return
        
        nome_busca = input("Digite o nome do livro: ").lower()
        encontrado = False
        for livro in filial.livros:
            if nome_busca in livro.titulo.lower():
                print(livro)
                encontrado = True
        if not encontrado:
            print("Livro não encontrado!")

    def buscarCategoria (self):
        if not self.filiais:
            print("Nenhuma filial cadastrada.")
            return
        print("Filiais disponíveis:")
        for filial in self.filiais:
            print(f"{filial.nome} - {filial.numero}")
        try:
            numero_filial = int(input("Digite o número da filial: "))
        except ValueError:
            print("Número da filial inválido.")
            return
        filial = next((f for f in self.filiais if f.numero == numero_filial), None)
        if not filial:
            print("Filial não encontrada.")
            return
        
        categoria_busca = input("Digite a categoria do livro: ").lower()
        encontrado = False
        for livro in filial.livros:
            if categoria_busca in livro.area.lower():
                print(livro)
                encontrado = True
        if not encontrado:
            print("Livro não encontrado!")

    def buscarPreco (self):
        if not self.filiais:
            print("Nenhuma filial cadastrada.")
            return
        print("Filiais disponíveis:")
        for filial in self.filiais:
            print(f"{filial.nome} - {filial.numero}")
        try:
            numero_filial = int(input("Digite o número da filial: "))
        except ValueError:
            print("Número da filial inválido.")
            return
        filial = next((f for f in self.filiais if f.numero == numero_filial), None)
        if not filial:
            print("Filial não encontrada.")
            return
        preco_busca = float(input("Digite o preço do livro: "))
        encontrado = False
        for livro in filial.livros:
            if preco_busca >= livro.valor:
                print(livro)
                encontrado = True
        if not encontrado:
            print("Livro não encontrado!")

    def buscarEstoque (self):
        if not self.filiais:
            print("Nenhuma filial cadastrada.")
            return
        print("Filiais disponíveis:")
        for filial in self.filiais:
            print(f"{filial.nome} - {filial.numero}")
        try:
            numero_filial = int(input("Digite o número da filial: "))
        except ValueError:
            print("Número da filial inválido.")
            return
        filial = next((f for f in self.filiais if f.numero == numero_filial), None)
        if not filial:
            print("Filial não encontrada.")
            return
        
        estoque_busca = int(input("Digite o estoque do livro: "))
        encontrado = False
        for livro in filial.livros:
            if estoque_busca <= livro.estoque:
                print(livro)
                encontrado = True
        if not encontrado:
            print("Livro não encontrado!")

    def valorTotalEstoque (self):
        if not self.filiais:
            print("Nenhuma filial cadastrada.")
            return
        print("Filiais disponíveis:")
        for filial in self.filiais:
            print(f"{filial.nome} - {filial.numero}")
        try:
            numero_filial = int(input("Digite o número da filial: "))
        except ValueError:
            print("Número da filial inválido.")
            return
        filial = next((f for f in self.filiais if f.numero == numero_filial), None)
        if not filial:
            print("Filial não encontrada.")
            return
            
        valorTotal = 0
        for livro in filial.livros:
            valorTotal += livro.valor * livro.estoque
        print(f"Valor total em estoque na {filial.nome}: R$ {valorTotal}")

    def carregarEstoque(self, arquivo="estoque.txt"):
        try:
            with open (arquivo, "r", encoding="utf-8") as storage:
                for linha in storage:
                    dados = linha.strip().split(",")
                    codigo = int(dados[0])
                    titulo = dados[1]
                    ano = int(dados[2])
                    area = dados[3]
                    editora = dados[4]
                    valor = float(dados[5])
                    estoque = int(dados[6])
                    numero_filial = int(dados[7])
                    filial = next((f for f in self.filiais if f.numero == numero_filial), None)
                    if filial is not None:
                        livro = Livro(codigo, titulo, ano, area, editora, valor, estoque, filial)
                        filial.adicionar_livro(livro)
            print("Estoque carregado com sucesso!")                        
        except FileNotFoundError:
            print("Arquivo não encontrado!")

    def atualizarEstoque(self, arquivo="estoque.txt", encoding="utf-8"):
        with open(arquivo, "w") as storage:
            for filial in self.filiais:
                for l in filial.livros:
                    linha = f"{l.codigo},{l.titulo},{l.ano},{l.area},{l.editora},{l.valor},{l.estoque},{l.filial}\n"
                    storage.write(linha)
            print("Estoque atualizado com sucesso!")
        
    #def listarPorFilial(self, numero_filial):

        
    #FILIAL
class gerenciarFiliais():
    
    def __init__(self):
        self.filiais = [
    Filial(101, "Filial Centro", "Rua A", "1234-5678", 100),
    Filial(102, "Filial Norte", "Rua B", "2345-6789", 200),
    Filial(103, "Filial Sul", "Rua C", "3456-7890", 150)
]
    
    def cadastrarFilial(self):
        self.numero = int(input("Codigo: "))
        self.nome = input("Nome: ")
        self.endereco = input("Endereco: ")
        self.contato = input("Contato: ")
        self.estoque = int(input("Estoque: "))
        
        nova_filial = Filial(self.numero, self.nome, self.endereco, self.contato, self.estoque)
        self.filiais.append(nova_filial)
        print("Filial cadastrada com sucesso!")
        
        
    def listarFiliais(self):
        for filial in self.filiais:
            print(filial)
            
    def atualizarFilial(self, arquivo="filiais.txt"):
        with open(arquivo, "w") as storage:
            for l in self.filiais:
                linha = f"{l.numero},{l.nome},{l.endereco},{l.contato},{l.estoque}\n"
                storage.write(linha)
        print("Filiais atualizadas com sucesso!")
        
    def carregarFiliais(self, arquivo="filiais.txt"):
        with open (arquivo, "r") as storage:
            for linha in storage:
                dados = linha.strip().split(",")
                numero = int(dados[0])
                nome = dados[1]
                endereco = dados[2]
                contato = dados[3]
                estoque = int(dados[4])
                self.filiais.append(Filial(numero, nome, endereco, contato, estoque))
        print("Você subiu as filiais com sucesso!")
    
if __name__ == "__main__":
    livraria = Livraria()
    gFilialis = gerenciarFiliais()
    livraria.filiais = gFilialis.filiais
    n = 1
    while n != 0:
        print("1 - Cadastrar Livros\n"
              "2 - Listar Livros\n"
              "3 - Buscar por Nome\n"
              "4 - Buscar por Categoria\n"
              "5 - Buscar por Preço\n"
              "6 - Buscar por Estoque\n"
              "7 - Valor total em Estoque\n"
              "8 - Carregar Estoque\n"
              "9 - Atualizar Estoque\n"
              "10 - Cadastrar Filial\n"
              "11 - Listar Filiais\n"
              "12 - Carregar Filiais\n"
              "13 - Atualizar Filiais\n"
              "14 - Buscar livro por Filial\n"
              "0 - Sair")
        n = int(input("Escolha uma opção: "))

        if n == 1:
            livraria.cadastroLivros()
        elif n == 2:
            livraria.listarLivros()
        elif n == 3:
            livraria.buscarNome()
        elif n == 4:
            livraria.buscarCategoria()
        elif n == 5:
            livraria.buscarPreco()
        elif n == 6:
            livraria.buscarEstoque()
        elif n == 7:
            livraria.valorTotalEstoque()
        elif n == 8:
            livraria.carregarEstoque()
        elif n == 9:
            livraria.atualizarEstoque()
        elif n == 10:
            gFilialis.cadastrarFilial()
        elif n == 11:
            gFilialis.listarFiliais()
        elif n == 12:
            gFilialis.carregarFiliais()
        elif n == 13:
            gFilialis.atualizarFilial()
        elif n == 14:
            livraria.listarPorFilial()
        elif n == 0:
            print("Programa encerrado!")
            break
        validar = input("Deseja continuar? [s/n]: ")
        if validar == "n":
            print("Programa encerrado!")
            break