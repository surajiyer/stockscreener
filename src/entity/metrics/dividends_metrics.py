def last_div_announced_date(period: str = 'D'):
    """Announcement Date of Last Dividend

    Announcement date of the last dividend.

    Args:
        period: str, default='D'
            D
    """
    pass

def last_div_cash_amount(period: str = 'D'):
    """Cash Amount of Last Dividend

    Cash dividend amount on a per-share basis.

    Args:
        period: str, default='D'
            D
    """
    pass

def last_div_cash_amount_split_adj(period: str = 'D'):
    """Cash Amount of Last Dividend (Split Adj)

    Cash dividend amount on a per-share basis, adjusted for stock splits.

    Args:
        period: str, default='D'
            D
    """
    pass

def gross_divid(period: str = 'LTM'):
    """Common Dividends Paid (CF)

    The cash outflow for dividends paid on a company's common stock

    Args:
        period: str, default='LTM'
            FY, Q, LTM, YTD
    """
    pass

def last_div_currency(period: str = 'D'):
    """Currency of Last Dividend

    Currency of the last dividend.

    Args:
        period: str, default='D'
            D
    """
    pass

def div_adj_factor(period: str = 'D'):
    """Dividend Adjustment Factor

    This item allows you to adjust the stock price return over a period of time to include income from dividends paid by the company.

    Args:
        period: str, default='D'
            D
    """
    pass

def div_share_cagr_10y():
    """Dividend CAGR (10y)

    Ten-year compound annual growth rate in dividend.
    """
    pass

def div_share_cagr_3y():
    """Dividend CAGR (3y)

    Three-year compound annual growth rate in dividend per share.
    """
    pass

def div_share_cagr_5y():
    """Dividend CAGR (5y)

    Five-year compound annual growth rate in dividend per share.
    """
    pass

def div_share_cagr_7y():
    """Dividend CAGR (7y)

    Seven-year compound annual growth rate in dividend per share.
    """
    pass

def dividend_coverage(period: str = 'LTM'):
    """Dividend Coverage Ratio

    A ratio that measures the cash cushion available to management to maintain the firm's dividend to common shareholders.

    Args:
        period: str, default='LTM'
            FY, Q, LTM, YTD
    """
    pass

def div_currency(period: str = 'D'):
    """Dividend Currency

    The currency in which a company declares a dividend.

    Args:
        period: str, default='D'
            D
    """
    pass

def div_frequency(period: str = 'D'):
    """Dividend Frequency

    The frequency with which a company typically pays dividends.

    Args:
        period: str, default='D'
            D
    """
    pass

def div_share_growth(period: str = 'LTM'):
    """Dividend Growth

    The growth rate in dividends per share.

    Args:
        period: str, default='LTM'
            FY, LTM
    """
    pass

def div_share(period: str = 'D'):
    """Dividend Per Share

    The dividend paid to shareholders for each share of stock. For quarterly dividend payers, it's common practice to multiply the most recent dividend by 4 to calculate dividend per share. Special dividends are not included in the calculation unless the company pays the dividend consistently in more than 1 period.

    Args:
        period: str, default='D'
            D
    """
    pass

def div_yield(period: str = 'LTM'):
    """Dividend Yield

    Measures the cash returned to shareholders by a firm as a percentage of the price they pay for each share of stock.

    Args:
        period: str, default='LTM'
            FY, LTM
    """
    pass

def last_div_ex_date(period: str = 'D'):
    """Ex-Date of Last Dividend

    Ex-dividend date is usually two business days before the dividend record date. Shares purchased on or after the ex-dividend date are not eligible to receive the next dividend payment.

    Args:
        period: str, default='D'
            D
    """
    pass

def last_div_payment_date(period: str = 'D'):
    """Payment Date of Last Dividend

    Date of the last dividend payment.

    Args:
        period: str, default='D'
            D
    """
    pass

def last_div_payment_type(period: str = 'D'):
    """Payment Type of Last Dividend

    Payment type of the last dividend. Value can be one of the following: cash, stock, spinoff, rights, and multiple dividends.

    Args:
        period: str, default='D'
            D
    """
    pass

def last_div_record_date(period: str = 'D'):
    """Record Date of Last Dividend

    Record date is the cut-off date used to determine which shareholders are entitled to receive a corporate dividend.

    Args:
        period: str, default='D'
            D
    """
    pass

def chowder_rule():
    """Chowder Rule Number

    A ratio that measures a company’s combined growth rate and dividend yield. We calculate the Chowder Rule Number by adding the dividend yield plus five-year dividend CAGR.
    """
    pass

def chowder_rule_fwd():
    """Chowder Rule Number (Fwd)

    A ratio that measures a company’s combined growth rate and dividend yield. We calculate the forward Chowder Rule Number by adding the dividend yield plus five-year forecast net income CAGR.
    """
    pass

def common_div(period: str = 'LTM'):
    """Common Dividends Paid

    Since the "gross_divid" metric is sourced from the cash flow statement, the common dividends are not always reported by the company on a standalone basis (i.e., they're lumped in with the "total_div_paid_cf" metric). This metric solves for the cash outflow for dividends paid on a company's common stock by deducting "pref_div" from "total_div_paid_cf."

    Args:
        period: str, default='LTM'
            FY, Q, LTM, YTD
    """
    pass

def div_yield_ex_special(period: str = 'D'):
    """Dividend Yield (Ex Special Dividends)

    Measures the cash returned to shareholders by a firm as a percentage of the price they pay for each share of stock.

    Args:
        period: str, default='D'
            D
    """
    pass

def div_share_ex_special(period: str = 'D'):
    """Dividend Per Share (Ex Special Dividends)

    The dividend paid to shareholders for each share of stock. For quarterly dividend payers, it's common practice to multiply the most recent dividend by 4 to calculate dividend per share. Special dividends are not included in the calculation.

    Args:
        period: str, default='D'
            D
    """
    pass

def div_share_ex_special_unadj(period: str = 'D'):
    """Dividend Per Share (Ex Special Dividends & Split Unadjusted)

    The dividend paid to shareholders for each share of stock. For quarterly dividend payers, it's common practice to multiply the most recent dividend by 4 to calculate dividend per share. Special dividends are not included in the calculation and no adjustments are made for stock splits.

    Args:
        period: str, default='D'
            D
    """
    pass

def div_yield_avg_10y():
    """Avg Dividend Yield (10y)

    Ten-year quarterly average dividend yield.
    """
    pass

def div_yield_avg_5y():
    """Avg Dividend Yield (5y)

    Five-year quarterly average dividend yield.
    """
    pass

def div_yield_avg_3y():
    """Avg Dividend Yield (3y)

    Three-year quarterly average dividend yield.
    """
    pass

def div_yield_median_10y():
    """Median Dividend Yield (10y)

    Ten-year quarterly median dividend yield.
    """
    pass

def div_yield_median_5y():
    """Median Dividend Yield (5y)

    Five-year quarterly median dividend yield.
    """
    pass

def div_yield_median_3y():
    """Median Dividend Yield (3y)

    Three-year quarterly median dividend yield.
    """
    pass

def upcoming_div_cash_amount():
    """Cash Amount of Upcoming Dividend

    Upcoming Cash dividend amount on a per-share basis.
    """
    pass

def upcoming_div_cash_amount_split_adj():
    """Cash Amount of Upcoming Dividend (Split Adj)

    Upcoming Cash dividend amount on a per-share basis, adjusted for stock splits.
    """
    pass

def upcoming_div_ex_date():
    """Ex-Date of Upcoming Dividend

    Upcoming ex-dividend date is usually two business days before the dividend record date. Shares purchased on or after the ex-dividend date are not eligible to receive the next dividend payment.
    """
    pass

def upcoming_div_payment_date():
    """Payment Date of Upcoming Dividend

    Upcoming date of the dividend payment.
    """
    pass

def upcoming_div_payment_type():
    """Payment Type of Upcoming Dividend

    Upcoming payment type of dividend. Value can be one of the following: cash, stock, spinoff, rights, and multiple dividends.
    """
    pass

def upcoming_div_record_date():
    """Record Date of Upcoming Dividend

    Upcoming record date is the cut-off date used to determine which shareholders are entitled to receive a corporate dividend.
    """
    pass

def gross_div_avg_5y():
    """Avg Common Dividends (5y)

    Five-year fiscal year average of common dividends paid.
    """
    pass

