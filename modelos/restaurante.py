from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}")
        for restaurante in cls.restaurantes:
            print(
                f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_item_no_cardapio(self, item) -> None:
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print('*' * 100)
        print(f'...Cardapio restaurante {self._nome}...')
        print('*' * 100)
        for index, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                print(f'Nome: {item.nome.ljust(25)}  Preco: {str(item.preco).ljust(15)}  Descricao: {item.descricao}')
            elif hasattr(item, 'quantidade'):
                print(f'Nome: {item.nome.ljust(25)}  Preco: {str(item.preco).ljust(15)}  Quantidade: {item.quantidade}')
            else:
                print(f'Nome: {item.nome.ljust(25)}  Preco: {str(item.preco).ljust(16)} Tipo: {item.tipo.ljust(25)} Tamanho: {item.tamanho}')




