"""VAT rates by product category, as the tax office publishes them (in percent)."""

from __future__ import annotations

from decimal import Decimal

RATES = {"standard": "20", "reduced": "5.5", "zero": "0"}


def rate_for(category: str) -> Decimal:
    """The VAT rate for `category`, as a fraction of the price."""
    return Decimal(RATES[category])
