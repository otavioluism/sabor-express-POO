from modelos.cardapio.item_cardapio import ItemCardapio


class Sobremesa(ItemCardapio):

    def __init__(self, nome: str, preco: float, tipo: str, tamanho: str) -> None:
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho

    def __str__(self):
        return self.preco

    def aplicar_desconto(self):
        self.preco -= (self.preco * 0.06)




