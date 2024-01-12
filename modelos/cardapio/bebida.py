from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):

    def __init__(self, nome: str, preco: float, quantidade: str):
        super().__init__(nome, preco)
        self.quantidade = quantidade

    def __str__(self):
        return self.nome

    def aplicar_desconto(self):
        self.preco -= (self.preco * 0.08)
