from src.boundary.fmp import FinancialModelingPrep
from src.entity.strategy import Strategy, strategies


class Screener:
    def __init__(self, strategy: str) -> None:
        self._strategy: Strategy = strategies[strategy]

    def get_stocks(self) -> list[str]:
        fmp = FinancialModelingPrep()
        stocks = fmp.get_stocks_list()
        stocks = self._strategy.apply(stocks)
        return stocks
