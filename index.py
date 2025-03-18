   
class Livros():
    def __init__(self, titulo, codigo, editora, area, ano, valor, estoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.estoque = estoque
     
if __name__ == "__main__":
    
    #Lista para adicionar os livros (Sor não é do GPT, eu uso anotações para me achar)
    
    livros = [
    Livros("Compiladores", "Cod#0301", "Pearson", "Computação", 2016, 85.00, 125),
    Livros("Engenharia de Software", "Cod#1203", "Pressman", "Computação", 2011, 78.00, 100)
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
            
        elif n == 2:
            print("Lista de Livros:")
            for livro in livros:    
                print("Título: ", livro.titulo)
                
        validar = input("Deseja continuar? (s/n)")
        if validar == "n":
            break
        else:
            continue