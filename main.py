from .intrinsic_value import intrinsic_value

intrisinc_v = intrinsic_value(estimates=[500 * 1.1 ** (i + 1) for i in range(9)],
                              forever=500 * 1.1 ** 10,
                              discount=0.10,
                              forever_inc_ratio=0.03)
print(intrisinc_v)
