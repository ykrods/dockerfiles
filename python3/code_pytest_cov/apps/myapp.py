"""
配送料計算とカバレッジ
"""
# enum
# JIS X 0401: 全国地方公共団体コード
JP_PREFECTURE_CODE_MAP = {
    1: "北海道",
    2: "青森",
    3: "岩手",
    4: "宮城",
    # ...
}

SHIPPING_FEE_MAP = {
    1: 1000,
    2: 900,
}


class Address():
    """ 住所 """
    def __init__(self,
                 pref_code,
                 city,
                 remines):
        """
        :param pref: 都道府県コード
        :param city: 市区町村
        :param remines: それ以降の住所(address2とかにしちゃう?)
        """
        self.pref_code = pref_code
        self.city = city
        self.remines = remines

    @property
    def too_near(self):
        return self.pref_code == 1


class Item():
    """ 商品 """
    def __init__(self, price):
        """
        :param price: 商品の金額
        """
        self.price = price


def total_price(items, shipping_address):
    """ 送料込みの金額
    """
    total = sum(item.price for item in items)

    # 3000 円以上の場合送料無料
    if 3000 <= total or shipping_address.too_near:
        return total

    return total + SHIPPING_FEE_MAP[shipping_address.pref_code]
