from library.fines import late_fee


def test_on_time_is_free():
    assert late_fee(0) == 0.0


def test_default_rule():
    assert late_fee(4) == 1.0


def test_the_desk_can_set_its_own_rule():
    assert late_fee(3, "days * 0.5 + 1") == 2.5
