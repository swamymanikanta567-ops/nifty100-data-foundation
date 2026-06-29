# Day 08 - Profitability Ratios

def net_profit_margin(net_profit, sales):
    if sales == 0:
        return None
    return round((net_profit / sales) * 100, 2)


def operating_profit_margin(operating_profit, sales):
    if sales == 0:
        return None
    return round((operating_profit / sales) * 100, 2)


def return_on_equity(net_profit, equity, reserves):
    total_equity = equity + reserves
    if total_equity <= 0:
        return None
    return round((net_profit / total_equity) * 100, 2)


def return_on_assets(net_profit, total_assets):
    if total_assets == 0:
        return None
    return round((net_profit / total_assets) * 100, 2)


def return_on_capital_employed(ebit, equity, reserves, borrowings):
    capital = equity + reserves + borrowings
    if capital == 0:
        return None
    return round((ebit / capital) * 100, 2)


# Day 09 - Leverage & Efficiency Ratios

def debt_to_equity(borrowings, equity, reserves):
    total_equity = equity + reserves
    if borrowings == 0:
        return 0
    if total_equity <= 0:
        return None
    return round(borrowings / total_equity, 2)


def interest_coverage(operating_profit, other_income, interest):
    if interest == 0:
        return None
    return round((operating_profit + other_income) / interest, 2)


def net_debt(borrowings, investments):
    return round(borrowings - investments, 2)


def asset_turnover(sales, total_assets):
    if total_assets == 0:
        return None
    return round(sales / total_assets, 2)