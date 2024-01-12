from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_praca.receber_avaliacao('Gui', 10)
# restaurante_praca.receber_avaliacao('Lais', 8)
# restaurante_praca.receber_avaliacao('Emy', 2)
bebida = Bebida('Suco de Melancia', 5.75, 'Grande')
prato = Prato('Pao de Forma', 2.75, 'O melhor pão de minas')


def main():
    # Restaurante.listar_restaurantes()
    restaurante_praca.adicionar_item_no_cardapio(prato)
    restaurante_praca.adicionar_item_no_cardapio(bebida)
    bebida.aplicar_desconto()
    prato.aplicar_desconto()
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
