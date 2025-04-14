from livros import Livro

class Livraria():
    def __init__ (self):
        self.livro = [
            Livro(9853, "Python para Zumbis", 2015, "Programação", "Editora3", 50.00, 10),
            Livro(2732, "Python Fluente", 2015, "Programação", "Editora2", 80.00, 5),
            Livro(32356, "Inteligência Artificial", 2018, "IA", "Editora1", 100.00, 3),
            Livro(4666, "Aprendizado de Máquina", 2019, "IA", "Editora1", 120.00, 2),
            Livro(51094, "Deep Learning", 2020, "IA", "Editora1", 150.00, 1)
        ]

    def cadastroLivros(self):
        self.titulo = input("Titulo: ")
        self.codigo = int(input("Codigo: "))
        self.editora = input("Editora: ")
        self.area = input("Area: ")
        self.ano = int(input("Ano: "))
        self.valor = float(input("Valor: "))
        self.estoque = int(input("Estoque: "))
        self.livro.append(Livro(self.titulo, self.codigo, self.editora, self.area, self.ano, self.valor, self.estoque))
        print("Livro cadastrado com sucesso!")

    def listarLivros (self):
        for livro in self.livro:
            print(livro)

    def buscarNome (self):
        nome_busca = input("Digite o nome do livro: ").lower()
        encontrado = False
        for livro in self.livro:
            if nome_busca in livro.titulo.lower():
                print(livro)
                encontrado = True
        if not encontrado:
            print("Livro não encontrado!")

    def buscarCategoria (self):
        categoria_busca = input("Digite a categoria do livro: ").lower()
        encontrado = False
        for livro in self.livro:
            if categoria_busca in livro.area.lower():
                print(livro)
                encontrado = True
        if not encontrado:
            print("Livro não encontrado!")

    def buscarPreco (self):
        preco_busca = float(input("Digite o preço do livro: "))
        encontrado = False
        for livro in self.livro:
            if preco_busca <= livro.valor:
                print(livro)
                encontrado = True
        if not encontrado:
            print("Livro não encontrado!")

    def buscarEstoque (self):
        estoque_busca = int(input("Digite o estoque do livro: "))
        encontrado = False
        for livro in self.livro:
            if estoque_busca <= livro.estoque:
                print(livro)
                encontrado = True
        if not encontrado:
            print("Livro não encontrado!")

    def valorTotalEstoque (self):
        valorTotal = 0
        for livro in self.livro:
            valorTotal += livro.valor * livro.estoque
        print(f"Valor total em estoque: R$ {valorTotal}")

    def carregarEstoque(self, arquivo="estoque.txt"):
        try:
            with open (arquivo, "r") as storage:
                for linha in storage:
                    dados = linha.strip().split(",")
                    codigo = int(dados[0])
                    titulo = dados[1]
                    ano = int(dados[2])
                    area = dados[3]
                    editora = dados[4]
                    valor = float(dados[5])
                    estoque = int(dados[6])
                    self.livro.append(Livro(titulo, codigo, editora, area, ano, valor, estoque))
            print("Estoque carregado com sucesso!")                        
        except FileNotFoundError:
            print("Arquivo não encontrado!")

    def atualizarEstoque(self, arquivo="estoque.txt"):
        with open(arquivo, "w") as storage:
            for l in self.livro:
                linha = f"{l.codigo},{l.titulo},{l.ano},{l.area},{l.editora},{l.valor},{l.estoque}\n"
                storage.write(linha)
        print("Estoque atualizado com sucesso!")        

if __name__ == "__main__":
    livraria = Livraria()
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
        elif n == 0:
            print("Programa encerrado!")
            break
        validar = input("Deseja continuar? [s/n]: ")
        if validar == "n":
            print("Programa encerrado!")
            break