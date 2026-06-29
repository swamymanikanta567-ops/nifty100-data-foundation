def cagr(start, end, years):
    if start <= 0 or years <= 0:
        return None
    return round((((end / start) ** (1 / years)) - 1) * 100, 2)