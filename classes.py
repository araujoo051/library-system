class Filial():
    def __init__(self, numero, nome, endereco, contato, estoque = 0):
        self.numero = numero
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.estoque = estoque
        
    def __str__(self):
        return (f">>>>>Cod# {self.numero}\n"
                f"Nome: {self.nome}\n"
                f"Endereco: {self.endereco}\n"
                f"Contato: {self.contato}\n"
                f"Estoque: {self.estoque}\n"
                f"===============================")

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
        

