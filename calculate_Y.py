global p, p_uncertainty, k
p = 1.01 * (10 ** 5)
p_uncertainty = 0.01
k = 1.38 * (10 ** -23)

def f_Y(gradient_bfl):
    global p, k
    Y = ((gradient_bfl * p) / k)
    return Y

def f_dY(Y, gradient_bfl, dm):
    global p, p_uncertainty
    dY = (((p_uncertainty/p) + (dm/gradient_bfl))/100) * Y
    return dY