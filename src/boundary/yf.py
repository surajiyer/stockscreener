import yfinance as yf


class YahooFinance:
    _cache = dict()

    def get_earnings_yield(self, ticker: str):
        ticker = yf.Ticker(ticker)
        ticker.info
        return ticker
