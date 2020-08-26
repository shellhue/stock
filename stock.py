
def return_ratio_with_dividends_considered(growth_ratio=0.1, yield_ratio=0.03, years=10):

    stock = 1.0
    price = 1.0

    start_capital = stock * price

    while (years > 0):
        # price after one year
        price = price * (1 + growth_ratio)

        # dividends
        dividends = stock * price * yield_ratio

        # exchange dividends for stock
        stock = stock + dividends / price

        years = years - 1

    end_capital = stock * price

    return end_capital / start_capital


if __name__ == "__main__":
    ratio = return_ratio_with_dividends_considered(
        growth_ratio=0.1, yield_ratio=0.1, years=10)
    print(ratio)
