from src.etl.normaliser import normalize_year, normalize_ticker


def test_normalize_year():
    assert normalize_year("2024") == 2024
    assert normalize_year(2025) == 2025
    assert normalize_year("abc") is None


def test_normalize_ticker():
    assert normalize_ticker("tcs") == "TCS"
    assert normalize_ticker(" infy ") == "INFY"
    assert normalize_ticker(None) is None