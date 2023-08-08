def f_temperature(Y, Z):
    p = 1.01 * (10 ** 5)
    k = 1.38 * (10 ** -23)
    d = 0.0279
    h = 0.06
    V = (3.142 * (d**2) * h) / 4
    temperature = ((p * V) / (Y * k)) - Z
    return temperature
