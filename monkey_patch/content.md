# Monkey Patch

Monkey Patch refers to modify classes or modules in runtime. Basically,
it is a dinamically replacement of attributes at runtime.

In the example let's have the class "Shop" were it is wanted to modify the
behaviour of report function:

```py
class Shop:
    def __init__(self, sales_number):
        self.sales_number = sales_number
    def report(self):
        return self.sales_number * 100

shop_1 = Shop(25)

print(shop_1.report()) # 2500
```

Now let's modify the class:

```py
def gains_report(self):
    return self.sales_number * 25

Shop.gains_report = gains_report
print(shop_1.gains_report()) # 625
```

Here, `gains_report` is added to the `Shop` class. This way, it will be available
through all the objects and instances of it
