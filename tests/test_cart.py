from decimal import Decimal

from checkout.cart import Cart


def make_cart() -> Cart:
    cart = Cart()
    cart.add("mug", "12.50", quantity=2)
    cart.add("tea", "8.00")
    return cart


def test_subtotal_adds_every_line():
    assert make_cart().subtotal == Decimal("33.00")


def test_total_adds_tax():
    assert make_cart().total() == Decimal("39.60")


def test_total_applies_a_discount_before_tax():
    assert make_cart().total(discount=Decimal("0.10")) == Decimal("35.64")


def test_an_empty_cart_costs_nothing():
    assert Cart().total() == Decimal("0.00")


def test_a_book_pays_the_reduced_rate():
    cart = Cart()
    cart.add("book", "20.00", category="reduced")
    assert cart.total() == Decimal("21.10")


def test_each_line_pays_its_own_rate():
    cart = Cart()
    cart.add("mug", "12.50")
    cart.add("book", "20.00", category="reduced")
    assert cart.total() == Decimal("36.10")
