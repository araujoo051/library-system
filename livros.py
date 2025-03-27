class Livro():
    def __init__ (self, titulo, codigo, editora, area, ano, valor, estoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.estoque = estoque

    def __str__ (self):
        valorTotalEstoque = self.valor * self.estoque
        return (f">>>>>Cod# {self.codigo}\n"
                f"Titulo/Editora: {self.titulo}/{self.editora}\n"
                f"Categoria: {self.area}\n"
                f"Ano: {self.ano}\n"
                f"Valor: R$ {self.valor}\n"
                f"Estoque: {self.estoque}\n"
                f"Valor Total em estoque: R$ {valorTotalEstoque}\n"
                f"===============================")
