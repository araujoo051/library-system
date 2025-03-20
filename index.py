class Livros():
    def __init__(self, titulo, codigo, editora, area, ano, valor, estoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.estoque = estoque
        
    def cadastroLivro(self):
        titulo = input("Digite o título do livro: ")
        codigo = input("Digite o código do livro: ")
        editora = input("Digite a editora do livro: ")
        area = input("Digite a área do livro: ")
        ano = int(input("Digite o ano do livro: "))
        valor = float(input("Digite o valor do livro: "))
        estoque = int(input("Digite a quantidade em estoque: "))
        livro = Livros(titulo, codigo, editora, area, ano, valor, estoque)
        livros.append(livro)
        print("Livro cadastrado com sucesso!")
        
#Listar livros
    def listarLivros(self):
        print("Lista de Livros:")
        for livro in livros:
            print(">>>>>", livro.codigo)    
            print("Título/Editora: ", livro.titulo,"/",livro.editora)
            print("Categoria: ", livro.area)
            print("Ano: ", livro.ano)
            print(f"Valor: R$, {livro.valor:.2f}")
            print("Estoque: ", livro.estoque)
            print("Valor total em estoque: R$", livro.valor * livro.estoque)
            print()
            
#Busca por nome
    def buscarLivroPorNome(self):
        nome_busca = input("Digite o nome do livro: ").lower()
        encontrado = False

        for livro in livros:
            if nome_busca in livro.titulo.lower(): 
                print(f"\nLivro encontrado:")
                print(f"Título: {livro.titulo}, Código: {livro.codigo}, Editora: {livro.editora}, "
                    f"Área: {livro.area}, Ano: {livro.ano}, Valor: R${livro.valor:.2f}, Estoque: {livro.estoque}")
                encontrado = True

        if not encontrado:
            print("Livro não encontrado")
    
#Busca por categoria    
    def buscarLivroPorCat(self):
        categoria_busca = input("Digite a categoria do livro: ").lower()
        encontrado = False

        for livro in livros:
            if categoria_busca in livro.area.lower(): 
                print(f"\nLivro encontrado:")
                print(f"Título: {livro.titulo}, Código: {livro.codigo}, Editora: {livro.editora}, "
                    f"Área: {livro.area}, Ano: {livro.ano}, Valor: R${livro.valor:.2f}, Estoque: {livro.estoque}")
                encontrado = True

        if not encontrado:
            print("Livro não encontrado")
            
#Busca por preço, livro com o preço até o valor informado
    def buscarLivroPorPreco(self):
        preco_busca = float(input("Digite o preço do livro: "))
        encontrado = False

        for livro in livros:
            5
            if livro.valor <= preco_busca: 
                print(f"\nLivro encontrado:")
                print(f"Título: {livro.titulo}, Código: {livro.codigo}, Editora: {livro.editora}, "
                    f"Área: {livro.area}, Ano: {livro.ano}, Valor: R${livro.valor:.2f}, Estoque: {livro.estoque}")
                encontrado = True
        
        if not encontrado:
            print("Livro não encontrado")

#Busca por quantidade total no estoque
    def buscarLivroPorEstoque(self):
        estoque_busca = int(input("Digite a quantidade em estoque: "))
        encontrado = False

        for livro in livros:
            if estoque_busca <= livro.estoque: 
                print(f"\nLivro encontrado:")
                print(f"Título: {livro.titulo}, Código: {livro.codigo}, Editora: {livro.editora}, "
                    f"Área: {livro.area}, Ano: {livro.ano}, Valor: R${livro.valor:.2f}, Estoque: {livro.estoque}")
                encontrado = True
        
        if not encontrado:
            print("Livro não encontrado")

#Busca por valor total no estoque
    def valorTotalEstoque(self):
        total = 0
        valor_busca = float(input("Qual valor total de estoque deseja buscar?"))
        encontrado = False

        for livro in livros:
            total = livro.valor * livro.estoque
            if valor_busca < total:
                print(f"\nLivro encontrado:")
                print(f"Código: {livro.codigo}, Título: {livro.titulo}, Editora: {livro.editora}, Categoria: {livro.area}, Ano: {livro.ano}, Valor total no estoque: R${total:.2f}")
                encontrado = True
        if not encontrado:
            print("Livro não encontrado")

     
if __name__ == "__main__":
    
    #Lista para adicionar os livros (Sor não é do GPT, eu uso anotações para me achar)
    
    livros = [
    Livros("Compiladores", "Cod#0301", "Pearson", "Computação", 2016, 85.00, 125),
    Livros("Engenharia de Software", "Cod#1203", "Pressman", "Computação", 2011, 78.00, 50)
    ]
    
    #Menu de entrada
    
    n = 1
    while n != 0:
        print("1 - Cadastrar Livro")
        print("2 - Listar Livros")
        print("3 - Buscar livro por nome")
        print("4 - Buscar livro por categoria")
        print("5 - Buscar livro por preço")
        print("6 - Busca por quantidade em estoque")
        print("7 - Valor total no estoque")
        print("0 - Encerrar atividades")
        n = int(input("Selecione uma opção: "))
        
    #Validação das opções do Menu
        
        if n == 1:
            livro = Livros("", "", "", "", 0, 0.0, 0)
            livro.cadastroLivro()     
        elif n == 2:
            livro = Livros("", "", "", "", 0, 0.0, 0)
            livro.listarLivros()
        elif n == 3:
            livro = Livros("", "", "", "", 0, 0.0, 0)
            livro.buscarLivroPorNome()
        elif n == 4:
            livro= Livros("", "", "", "", 0, 0.0, 0)
            livro.buscarLivroPorCat()
        elif n == 5:
            livro = Livros("", "", "", "", 0, 0.0, 0)
            livro.buscarLivroPorPreco()
        elif n == 6:
            livro = Livros("", "", "", "", 0, 0.0, 0)
            livro.buscarLivroPorEstoque()
        elif n == 7:
            livro = Livros("", "", "", "", 0, 0.0, 0)
            livro.valorTotalEstoque()
        elif n == 0:
            print("Programa encerrado!")
            break  
        validar = input("Deseja continuar? (s/n)")
        if validar == "n":
            break
        else:
            continue