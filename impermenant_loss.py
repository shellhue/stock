import matplotlib.pyplot as plt


class Pair(object):
    def __init__(self, a_amount, b_amount, a_symbol, b_symbol):
        self._a_amount = a_amount
        self._b_amount = b_amount
        self.a_symbol = a_symbol
        self.b_symbol = b_symbol

    def a_price(self):
        return self._a_amount * 1.0 / self._b_amount

    def b_price(self):
        return self._b_amount * 1.0 / self._a_amount

    def paying_amount_to_buy_b(self, amount):
        return self._paying_amount_to_buy(amount, self._b_amount, self._a_amount)

    def paying_amount_to_buy_a(self, amount):
        return self._paying_amount_to_buy(amount, self._a_amount, self._b_amount)

    def _paying_amount_to_buy(self, buying_amount, buying_stock, paying_stock):
        k = self._a_amount * self._b_amount * 1.0
        return k * 1.0 / (buying_stock - buying_amount) - paying_stock

    def paying_amount_to_buy_b_at_price(self, price):
        pass

    def balance_after_buying_b(self, amount):
        paying_a = self.paying_amount_to_buy_b(amount)
        a_reserve = self._a_amount + paying_a
        b_reserve = self._b_amount - amount
        print(a_reserve * b_reserve)
        print("new balance {}: {}, {}: {} price: {}".format(self.a_symbol, a_reserve, self.b_symbol, b_reserve, a_reserve / b_reserve))
        return a_reserve, b_reserve

    def impermenant_loss_after_buying_b(self, amount):
        a_reserve, b_reserve = self.balance_after_buying_b(amount)
        total_val_in_a_if_just_holding = self._a_amount + self._b_amount * 1.0 * a_reserve / b_reserve
        current_total_val_in_a = 2.0 * a_reserve

        return (current_total_val_in_a - total_val_in_a_if_just_holding) / total_val_in_a_if_just_holding

    @classmethod
    def impermenant_loss_for_price_change(cls, change):
        r = change + 1.0
        return -1.0 * (r ** 0.5 - 1) ** 2 / (r + 1)

    @classmethod
    def impermenant_loss_for_price_change_in_ratio(cls, change_ratio):
        r = change_ratio
        return -1.0 * (r ** 0.5 - 1) ** 2 / (r + 1)


if __name__ == "__main__":
    price_change = []
    impermenant_loss = []
    i = -1.0
    while i < 5.0:
        price_change.append(i)
        impermenant_loss.append(Pair.impermenant_loss_for_price_change(i))
        i += 0.001
    # plt.scatter(price_change, impermenant_loss, linewidths=0.51)
    plt.plot(price_change, impermenant_loss)
    plt.savefig("./test.jpg")
    for i in [-0.1, 0.1]:
        loss = Pair.impermenant_loss_for_price_change(change=i)
        print("impermenant loss: {:0.2f}% (price change) {} (loss)".format(i * 100))
    print(Pair.impermenant_loss_for_price_change(change=-10.0/100.0))
    print(Pair.impermenant_loss_for_price_change(change=-50.0/100.0))
