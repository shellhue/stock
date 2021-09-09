

def cal_apy(base, diposit, diposit_apr, lend, lend_apr):
    return (diposit * diposit_apr + lend * lend_apr) / base, diposit / base, (diposit * diposit_apr + lend * lend_apr) / diposit


if __name__ == "__main__":
    eth = 27
    beth = 70
    price = 2920

    ren_ratio = 6.5
    safe_ratio = 0.5

    lenable_usd_in_venus = 0.8 * eth * price + 0.6 * beth * price
    lenable_usd_in_venus2 = 0.8 * eth * price + 0.8 * (beth * 0.6) * price
    lenable_usd_in_venus3 = 0.8 * eth * price + 0.8 * (beth * 0.94) * price

    print("lendable usd in venus:", lenable_usd_in_venus * ren_ratio * safe_ratio)
    print("lendable usd in venus2:", lenable_usd_in_venus2 * ren_ratio * safe_ratio)
    print("lendable usd in venus3:", lenable_usd_in_venus3 * ren_ratio * safe_ratio)
    

