"""The header printed at the top of every receipt."""

from __future__ import annotations

from datetime import date


def header(shop: str) -> str:
    """The shop's name and today's date, as the receipt prints them."""
    return f"{shop} · {date.today():%d/%m/%Y}"
