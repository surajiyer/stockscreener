from io import BytesIO
import ftplib
import pandas as pd


class NasdaqTrader:
    def get_stocks_list(self) -> pd.DataFrame:
        ftp = ftplib.FTP("ftp.nasdaqtrader.com")
        ftp.login("anonymous", "")
        ftp.cwd("SymbolDirectory")
        tickers = []
        with BytesIO() as f:
            ftp.retrbinary("RETR nasdaqlisted.txt", f.write)
            f.seek(0)
            df = pd.read_csv(f, sep="|")
            df = df[df["ETF"] == "N"]
            tickers.append(df["Symbol"])
        with BytesIO() as f:
            ftp.retrbinary("RETR otherlisted.txt", f.write)
            f.seek(0)
            df = pd.read_csv(f, sep="|")
            df = df[df["ETF"] == "N"]
            tickers.append(df["ACT Symbol"])
        ftp.quit()
        tickers = pd.concat(tickers, ignore_index=True).sort_values()
        return pd.DataFrame(index=tickers)
