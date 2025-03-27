from livros import Livro

class Livraria():
    def __init__ (self):
        self.livro = [
            Livro("Python para Zumbis", 1, "Editora3", "Programação", 2015, 50.00, 10),
            Livro("Python Fluente", 2, "Editora2", "Programação", 2015, 80.00, 5),
            Livro("Inteligência Artificial", 3, "Editora1", "IA", 2018, 100.00, 3),
            Livro("Aprendizado de Máquina", 4, "Editora1", "IA", 2019, 120.00, 2),
            Livro("Deep Learning", 5, "Editora1", "IA", 2020, 150.00, 1)
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
        elif n == 0:
            print("Programa encerrado!")
            break
        validar = input("Deseja continuar? [s/n]: ")
        if validar == "n":
            print("Programa encerrado!")
            break
        
    

        


