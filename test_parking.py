import pytest
from parking import parking_fee

def test_free_first_15_minutes():
    assert parking_fee(15) == 0

def test_fee_starts_at_16_minutes():
    assert parking_fee(16) == 10

def test_fee_for_75_minutes():
    assert parking_fee(75) == 20

def test_daily_rate_at_exactly_8_hours():
    assert parking_fee(480) == 80

def test_daily_rate_after_8_hours():
    assert parking_fee(481) == 80

def test_negative_minutes_raise_error():
    with pytest.raises(ValueError, match="Час не може бути негативним"):
        parking_fee(-1)