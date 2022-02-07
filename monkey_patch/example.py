class Shop:
    def __init__(self, sales_number):
        self.sales_number = sales_number

    def report(self):
        return self.sales_number * 100


shop_1 = Shop(25)

print(shop_1.report())  # 2500


def gains_report(self):
    return self.sales_number * 25


Shop.gains_report = gains_report

print(shop_1.gains_report())
