"""A shopping cart: line items, discounts and tax."""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import ROUND_HALF_UP, Decimal

from checkout.tax import rate_for

CENT = Decimal("0.01")


@dataclass(frozen=True)
class Item:
    sku: str
    unit_price: Decimal
    quantity: int = 1
    category: str = "standard"

    @property
    def subtotal(self) -> Decimal:
        return self.unit_price * self.quantity


@dataclass
class Cart:
    items: list[Item] = field(default_factory=list)

    def add(self, sku: str, unit_price: str, quantity: int = 1, category: str = "standard") -> None:
        self.items.append(Item(sku, Decimal(unit_price), quantity))

    @property
    def subtotal(self) -> Decimal:
        return sum((i.subtotal for i in self.items), Decimal(0))

    def total(self, discount: Decimal = Decimal(0)) -> Decimal:
        """Each line less `discount` (a fraction: 0.10 is 10% off), plus its own VAT."""
        total = sum(
            (i.subtotal * (1 - discount) * (1 + rate_for(i.category)) for i in self.items),
            Decimal(0),
        )
        return total.quantize(CENT, ROUND_HALF_UP)
