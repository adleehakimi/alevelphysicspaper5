global p, k
p = 1.01 * (10 ** 5)
k = 1.38 * (10 ** -23)

def f_Z(y_intercept, mbfl):
    global p, k
    Z = y_intercept/mbfl
    return Z

def f_dZ(y_intercept, dy_intercept, mbfl, dm, Z):
    dZ = (((dy_intercept/y_intercept) + (dm/mbfl))/100) * Z
    return dZ