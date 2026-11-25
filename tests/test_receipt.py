from freezegun import freeze_time

from checkout.receipt import header


@freeze_time("2026-11-25")
def test_a_receipt_is_dated_the_day_it_prints():
    assert header("Corner Shop") == "Corner Shop · 25/11/2026"
