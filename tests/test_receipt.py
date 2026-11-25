from decimal import Decimal

from checkout.cart import Item, receipt_line


def test_a_receipt_line_names_quantity_sku_and_subtotal(snapshot):
    assert receipt_line(Item("mug", Decimal("12.50"), 2)) == snapshot
