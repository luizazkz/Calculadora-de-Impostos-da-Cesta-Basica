"""
Semana 1 — Modelando produtos (Orientação a Objetos)

Complete os trechos marcados com TODO.
Não altere os nomes das classes, métodos e constantes: a correção é automática.
"""

ALIQUOTA_PADRAO = 0.25  # alíquota padrão hipotética (IBS + CBS)


class Produto:
    """Classe base de todos os produtos do supermercado."""

    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self) -> float:
        """Preço do produto SEM imposto."""
        return self._preco

    @preco.setter
    def preco(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor

    def aliquota(self) -> float:
        """Cada subclasse define sua própria alíquota."""
        raise NotImplementedError("Cada subclasse deve definir sua alíquota.")

    def imposto(self) -> float:
        """Imposto de UMA unidade: round(preco * aliquota, 2)."""
        return round(self.preco * self.aliquota(), 2)

    def preco_final(self) -> float:
        """Preço + imposto, arredondado em 2 casas."""
        return round(self.preco + self.imposto(), 2)

    def __str__(self) -> str:
        """Formato: 'Arroz 5kg - R$ 20.90 (imposto: R$ 0.00)'"""
        return f"{self.nome} - R$ {self.preco:.2f} (imposto: R$ {self.imposto():.2f})"


class ProdutoCestaBasica(Produto):
    """Item da Cesta Básica Nacional: alíquota zero."""

    def aliquota(self) -> float:
        return 0.0


class ProdutoReduzido(Produto):
    """Alimento com redução de 60%: paga 40% da alíquota padrão."""

    def aliquota(self) -> float:
        return 0.4 * ALIQUOTA_PADRAO


class ProdutoPadrao(Produto):
    """Produto sem benefício: paga a alíquota padrão."""

    def aliquota(self) -> float:
        return ALIQUOTA_PADRAO


if __name__ == "__main__":
    # TESTES
    arroz = ProdutoCestaBasica("Arroz 5kg", 20.90)
    refri = ProdutoPadrao("Refrigerante 2L", 7.00)
    banana = ProdutoCestaBasica("Banana KG", 10.00)
    bolinho = ProdutoPadrao("Bolinho UND", 1.00)
    oleo = ProdutoCestaBasica("Oleo de Cozinha 2L", 5.00)
    print(arroz)
    print(refri)
    print(banana)
    print(bolinho)
    print(oleo)
