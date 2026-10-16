from library.basket import load_basket, save_basket


def test_basket_survives_a_visit():
    assert load_basket(save_basket([3, 1, 4])) == [3, 1, 4]


def test_no_cookie_is_an_empty_basket():
    assert load_basket("") == []
