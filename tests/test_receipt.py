from datetime import date
from unittest.mock import patch

from checkout.receipt import header


def test_a_receipt_is_dated_the_day_it_prints():
    with patch("checkout.receipt.date") as mock_date:
        mock_date.today.return_value = date(2026, 11, 25)
        assert header("Corner Shop") == "Corner Shop · 25/11/2026"
