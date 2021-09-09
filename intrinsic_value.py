from typing import List


def intrinsic_value(estimates: List[float],
                    forever: float,
                    discount: float,
                    forever_inc_ratio: float):
    print([int(i) for i in estimates], forever)
    value = 0
    for i, v in enumerate(estimates):
        value += v / (1 + discount) ** (i + 1)
    last = 0
    for i in range(len(estimates) + 1, len(estimates) + 1 + 5000):
        r = 1 + forever_inc_ratio
        d = discount + 1
        dis = forever * (r / d) ** i * r ** (-len(estimates) - 1)
        last += dis
    print(value, last, last / (value + last), (value + last) / forever * discount)
    return value + last


if __name__ == "__main__":
    intrisinc_v = intrinsic_value(estimates=[500 * 1.1 ** (i + 1) for i in range(9)],
                                  forever=500 * 1.1 ** 10,
                                  discount=0.10,
                                  forever_inc_ratio=0.03)
    print(intrisinc_v)
