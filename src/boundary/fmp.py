import fmpsdk
import os
import pandas as pd


API_KEY = os.environ.get("FMP_API_KEY", "")


class FinancialModelingPrep:
    def get_stocks_list(self) -> pd.DataFrame:
        return pd.DataFrame(
            fmpsdk.company_valuation.available_traded_list(apikey=API_KEY)
        ).set_index("symbol")
