def calculate_si(p, t, r):
    si = (p * t * r) / 100
    return si


print(' when p = 10000, t = 2yrs, r = 8% => si =', calculate_si(10000, 2, 8))