"""
Semana 2 — O carrinho de compras (Orientação a Objetos: composição)

Complete os trechos marcados com TODO.
Não altere os nomes da classe e dos métodos: a correção é automática.
"""

from produtos import ALIQUOTA_PADRAO, Produto


class Carrinho:
    """Guarda produtos e suas quantidades."""

    def __init__(self):
        # Computador  nome -> [produto, quantidade]
        self._itens = {}

    def adicionar(self, produto: Produto, quantidade: int = 1) -> None:
        """
        - TypeError se produto não for instância de Produto
        - ValueError se quantidade não for inteiro >= 1
        - Se já existir produto com o mesmo nome, soma a quantidade
        """
       
        if not isinstance(produto, Produto):
            raise TypeError("Só é possível adicionar objetos do tipo Produto.")
            
        if not isinstance(quantidade, int) or isinstance(quantidade, bool) or quantidade < 1:
            raise ValueError("A quantidade deve ser um inteiro maior ou igual a 1.")

        if produto.nome in self._itens:
            self._itens[produto.nome][1] += quantidade
        else:
            self._itens[produto.nome] = [produto, quantidade]

    def remover(self, nome: str) -> None:
        """Remove o produto inteiro. KeyError se não existir."""
        del self._itens[nome]

    def subtotal(self) -> float:
        """Soma de preco * quantidade (sem impostos)."""
        return round(
            sum(produto.preco * qtd for produto, qtd in self._itens.values()), 2
        )

    def total_impostos(self) -> float:
        """Soma de produto.imposto() * quantidade."""
        return round(
            sum(produto.imposto() * qtd for produto, qtd in self._itens.values()), 2
        )

    def total(self) -> float:
        """subtotal() + total_impostos()"""
        return round(self.subtotal() + self.total_impostos(), 2)

    def economia(self) -> float:
        """
        Quanto o consumidor pagaria A MAIS se todos os produtos
        tivessem a alíquota padrão:
            soma de round(preco * ALIQUOTA_PADRAO, 2) * quantidade
            menos total_impostos()
        """
        imposto_se_fosse_padrao = sum(
            round(produto.preco * ALIQUOTA_PADRAO, 2) * qtd
            for produto, qtd in self._itens.values()
        )
        return round(imposto_se_fosse_padrao - self.total_impostos(), 2)

    def __len__(self) -> int:
        """Total de UNIDADES no carrinho."""
        return sum(qtd for _, qtd in self._itens.values())

    def __contains__(self, nome: str) -> bool:
        """Permite: 'Arroz 5kg' in carrinho"""
        return nome in self._itens


if __name__ == "__main__":
    from produtos import ProdutoCestaBasica, ProdutoPadrao

    c = Carrinho()
    c.adicionar(ProdutoCestaBasica("Feijão 1kg", 8.00), 2)
    c.adicionar(ProdutoPadrao("Chocolate", 10.00))
    print("Total:", c.total())
    print("Economia:", c.economia())
