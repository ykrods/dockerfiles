import pytest


@pytest.fixture(scope='function')
def items(request):
    from apps.myapp import Item
    return [Item(price=p) for p in request.param]


@pytest.fixture(scope='function')
def address(request):
    from apps.myapp import Address
    return Address(pref_code=request.param, city="", remines="")


@pytest.mark.parametrize('items, address, expected', [
    ([10000], 2, 10900),
    ([1000, 2000], 2, 3000)
], indirect=['items', 'address'])
def test_total_price(items, address, expected):
    from apps.myapp import total_price

    assert total_price(items, address) == expected
