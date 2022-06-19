import pandas as pd
from src.entity.strategy.strategy import Strategy
from src.entity.metrics.misc_metrics import sector
from src.entity.metrics.valuation_metrics import earnings_yield_ltm
from src.entity.metrics.efficiency_metrics import return_capital


class GreenblattMagicFormula(Strategy):
    def apply(self, df_stocks: pd.DataFrame) -> pd.DataFrame:
        """Joel Greenblatt Magic Formula

        Link(s):
            1. https://www.magicformulainvesting.com/

        Steps:
            1. Restrict stocks to BSE 200.
            2. Exclude banking and financial stocks.
            3. Determine earnings yield LTM of companies: EBIT / Enterprise value.
            4. Determine return on capital LTM: EBIT / return on capital employed.
            5. Stocks are ranked in order of companies return on capital.
            6. Rank the same stocks in order of the companies earnings yield.
            7. Add the two rankings and sort again. The top 10 companies should reflect the best of both.
            8. Rebalance portfolio anually and stay invested for 3-5 years.
        """
        df_stocks = df_stocks.copy()

        if "sector" not in df_stocks:
            df_stocks["sector"] = df_stocks.index.apply(sector)
        df_stocks = df_stocks[~df_stocks["sector"].isin(["Banking", "Financial"])]

        if "earnings_yield_ltm" not in df_stocks:
            df_stocks["earnings_yield_ltm"] = df_stocks.index.apply(earnings_yield_ltm)

        if "return_capital" not in df_stocks:
            df_stocks["return_capital"] = df_stocks.index.apply(return_capital)

        df_stocks["GreenblattMagicFormulaScore"] = (
            df_stocks["earnings_yield_ltm"].rank() + df_stocks["return_capital"].rank()
        )
        df_stocks.sort_values(
            "GreenblattMagicFormulaScore",
            ignore_index=False,
            inplace=True,
            ascending=False,
        )

        return df_stocks
