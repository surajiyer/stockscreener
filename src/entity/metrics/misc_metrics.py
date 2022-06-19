def description(ticker: str):
    """Description

    A brief description of a company or stock.
    """
    pass


def entity_type(ticker: str):
    """Entity Type

    The type of entity (company, etf, closed-end fund, etc.)
    """
    pass


def first_trade_date(ticker: str):
    """First Trade Date (Trading Item)

    The date the subject security started trading on an exchange
    """
    pass


def forecast_currency(ticker: str):
    """Forecast Currency

    The currency in which a company's analysts forecast data for the company.
    """
    pass


def full_ticker(ticker: str):
    """Full Ticker

    The fully qualified ticker in EXCHANGE:SYMBOL format
    """
    pass


def employees(period: str = "FY"):
    """Full Time Employees

    The number of full time employees that the company employs. This metric is only available when the data is reported in company filings.

    Args:
        period: str, default='FY'
            FY, Q
    """
    pass


def indexes(ticker: str):
    """Index Membership

    The indices that use a stock as part of its price calculation.
    """
    pass


def industry(ticker: str):
    """Industry (GICS)

    The industry in which a company operates.
    """
    pass


def industry_group(ticker: str):
    """Industry Group (GICS)

    The industry group in which a company operates.
    """
    pass


def inv_method(period: str = "Q"):
    """Inventory Method

    The inventory record keeping method used by the company (FIFO / LIFO).

    Args:
        period: str, default='Q'
            FY, Q
    """
    pass


def last_period_end_date(ticker: str):
    """Last Period End Date

    The most recent reporting period end date
    """
    pass


def last_fiscal_period(ticker: str):
    """Last Reported Fiscal Period Key

    The most recent reporting period fiscal period in our period format. Latest final key Example: FY${fiscal_year}.Q${fiscal_qtr}
    """
    pass


def last_fiscal_qtr(ticker: str):
    """Last Reported Fiscal Quarter

    The most recent reporting period fiscal quarter
    """
    pass


def last_fiscal_year(ticker: str):
    """Last Reported Fiscal Year

    The most recent reporting period fiscal year
    """
    pass


def name(ticker: str):
    """Name

    The name of the company of stock.
    """
    pass


def relisted(ticker: str):
    """New Trading Ticker

    If applicable, new ticker symbol of trading item
    """
    pass


def country(ticker: str):
    """Operating Country

    Country name where the company primarily operates
    """
    pass


def country_iso(ticker: str):
    """Operating Country ISO Code

    Three letter ISO Code of the country where the company primarily operates
    """
    pass


def operating_region(ticker: str):
    """Operating Region

    The operating region name of the company
    """
    pass


def operating_region_id(ticker: str):
    """Operating Region ID

    The operating region id of the company
    """
    pass


def period_end_date(period: str = "Q"):
    """Period End Date

    The date of the reporting period.

    Args:
        period: str, default='Q'
            FY, Q, LTM, YTD
    """
    pass


def primary_ticker(ticker: str):
    """Primary Ticker of Company

    The ticker of the primary trading item for the company.
    """
    pass


def is_primary(ticker: str):
    """Primary Trading Item Flag

    Returns the value TRUE if the trading item is a Primary Ticker of Company
    """
    pass


def reporting_currency(ticker: str):
    """Reporting Currency

    The currency in which a company's reports its financial statements.
    """
    pass


def reporting_frequency(ticker: str):
    """Reporting Frequency

    The frequency with which a company's reports its financial statements.
    """
    pass


def reporting_scale(ticker: str):
    """Reporting Scale

    The unit in which a company's reports its financial statements (thousands, millions, billions, etc.).
    """
    pass


def sector(ticker: str):
    """Sector

    The sector in which a stock operates.
    """
    pass


def sector_id(ticker: str):
    """Sector ID

    The unique sector id assigned to a company.
    """
    pass


def last_trade_date(ticker: str):
    """Security End Date

    Last trading date of a delisted security.
    """
    pass


def features(ticker: str):
    """Security Features

    Special features associated with the security
    """
    pass


def security_name(ticker: str):
    """Security Name

    Name of trading item's security
    """
    pass


def security_start_date(ticker: str):
    """Security Start Date

    The date the subject security was issued
    """
    pass


def security_subtype(ticker: str):
    """Security Subtype

    Type of trading item's security
    """
    pass


def benchmarks(ticker: str):
    """Similar Companies

    Companies similar to the subject company.
    """
    pass


def benchmark_ids(ticker: str):
    """Similar Companies IDs

    Ids of companies that are similar to the subject company.
    """
    pass


def exchange(ticker: str):
    """Stock Exchange Code

    The primary stock exchange where a stock is listed.
    """
    pass


def ticker(ticker: str):
    """Ticker

    The ticker symbol a stock trades under on its primary stock exchange.
    """
    pass


def trading_country(ticker: str):
    """Trading Country

    Trading country name of the trading item
    """
    pass


def trading_country_iso(ticker: str):
    """Trading Country ISO Code

    Trading country id (ISO 3-letter Code)
    """
    pass


def trading_currency(ticker: str):
    """Trading Currency

    The currency in which the security trades on the subject exchange.
    """
    pass


def region(ticker: str):
    """Trading Region

    The region of the exchange where the trading item trades.
    """
    pass


def trading_to_reporting_pair(ticker: str):
    """Trading to Reporting Currency Pair

    The foreign exchange pair of security's trading currency and reporting currency.
    """
    pass


def region_id(ticker: str):
    """Trading Region Id

    The region id of the exchange where the trading item trades.
    """
    pass


def exchange_name(ticker: str):
    """Stock Exchange Name

    Name of stock exchange where the trading item trades.
    """
    pass


def economic_region(ticker: str):
    """Economic Risk Region

    The economic region of the country in which the company operates. Economic risk region is one of the following values: Developed, Frontier and Developing.
    """
    pass
