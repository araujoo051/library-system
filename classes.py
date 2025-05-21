class Livro():
    def __init__ (self, codigo, titulo, ano, area, editora, valor, estoque, filial):
        self.codigo = codigo
        self.titulo = titulo
        self.ano = ano
        self.area = area
        self.editora = editora
        self.valor = valor
        self.estoque = estoque
        self.filial = filial

    def __str__ (self):
        valorTotalEstoque = self.valor * self.estoque
        return (f">>>>>Cod# {self.codigo}\n"
                f"Titulo/Editora: {self.titulo}/{self.editora}\n"
                f"Ano: {self.ano}\n"
                f"Area: {self.area}\n"
                f"Editora: R$ {self.editora}\n"
                f"Valor: R$ {self.valor}\n"
                f"Estoque: {self.estoque}\n"
                f"Filial: {self.filial.numero}\n"
                f"Valor Total em estoque: R$ {valorTotalEstoque}\n"
                f"===============================")
class Filial():
    def __init__(self, numero, nome, endereco, contato, estoque):
        self.numero = numero
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.estoque = estoque
        self.livros = []
        
    def adicionar_livro(self, livro):
        self.livros.append(livro)
        
    def listar_livros(self):
        if self.livros is not None:
            print(f"Livros na Filial {self.numero}:")
            for livro in self.livros:
                print(livro.titulo)
        else:
            print(f"Nenhum livro cadastrado na Filial {self.numero}.")
        
    def __str__(self):
        return (f">>>>>Cod# {self.numero}\n"
                f"Nome: {self.nome}\n"
                f"Endereco: {self.endereco}\n"
                f"Contato: {self.contato}\n"
                f"Estoque: {self.estoque}\n"
                f"===============================")



