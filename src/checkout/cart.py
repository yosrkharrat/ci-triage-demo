"""A shopping cart: line items, discounts and tax."""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")


@dataclass(frozen=True)
class Item:
    sku: str
    unit_price: Decimal
    quantity: int = 1

    @property
    def subtotal(self) -> Decimal:
        return self.unit_price * self.quantity


@dataclass
class Cart:
    items: list[Item] = field(default_factory=list)
    tax_rate: Decimal = Decimal("0.20")

    def add(self, sku: str, unit_price: str, quantity: int = 1) -> None:
        self.items.append(Item(sku, Decimal(unit_price), quantity))

    @property
    def subtotal(self) -> Decimal:
        return sum((i.subtotal for i in self.items), Decimal(0))

    def total(self, discount: Decimal = Decimal(0)) -> Decimal:
        """Subtotal, less `discount` (a percentage: 10 is 10% off), plus tax."""
        discounted = self.subtotal * (1 - discount / 100)
        return (discounted * (1 + self.tax_rate)).quantize(CENT, ROUND_HALF_UP)
