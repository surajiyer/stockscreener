from abc import ABC, abstractmethod
import pandas as pd


class Strategy(ABC):
    @abstractmethod
    def apply(self, df_stocks: pd.DataFrame) -> pd.DataFrame:
        pass
