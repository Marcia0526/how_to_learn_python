from abc import abstractmethod
from collections import namedtuple


# 产品SKU信息：产品id+数量+单价
class LineItem:
    def __init__(self, product_name, product_num, product_price):
        self.product_name = product_name
        self.product_num = product_num
        self.product_price = product_price

    def total_price(self):
        return self.product_num * self.product_price


# 顾客信息：姓名+积分
Customer = namedtuple('Customer', 'Fidelity')


# 订单
class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    # 订单总额
    def total_amount(self):
        return sum(item.total_price() for item in self.cart)

    # 订单实付总额
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total_amount() - discount

    def __str__(self):
        fmt = '<订单 总价: {:.2f} 实付: {:.2f}>'
        return fmt.format(self.total_amount(), self.due())


# 积分折扣策略
def fidelity_prom(order):
    if order.customer.Fidelity >= 1000:
        return order.total_amount() * 0.05
    else:
        return 0
        # return order.total_amount()*0.05 if order.customer.fidelity >= 1000 else 0


# 单个产品数量超过20的折扣策略
def single_item_prom(order):
    discount = 0
    for item in order.cart:
        if item.product_num >= 20:
            discount += item.total_price() * 0.1
    return discount


# 产品种类超过10的折扣策略
def bulk_item_prom(order):
    discount = 0
    sum_num = len({item.product_name for item in order.cart})
    if sum_num >= 10:
        discount = order.total_amount() * 0.3
    return discount


Tim = Customer(1000)
fruit_cart = [LineItem('apple', 30, 5), LineItem('banana', 10, 2.9)]
print(Order(Tim, fruit_cart, fidelity_prom))
print(Order(Tim, fruit_cart, single_item_prom))
