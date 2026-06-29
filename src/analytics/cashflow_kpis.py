def free_cash_flow(operating_activity, investing_activity):
    return operating_activity + investing_activity


def capex_intensity(investing_activity, sales):
    if sales == 0:
        return None
    return round((abs(investing_activity) / sales) * 100, 2)


def fcf_conversion(fcf, operating_profit):
    if operating_profit == 0:
        return None
    return round((fcf / operating_profit) * 100, 2)