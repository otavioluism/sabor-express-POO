from modelos.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):

    def __init__(self, nome: str, preco: float, descricao: str):
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return self.nome

    def aplicar_desconto(self):
        self.preco -= (self.preco * 0.05)
