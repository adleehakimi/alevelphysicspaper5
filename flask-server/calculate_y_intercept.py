def f_y_intercept_bfl(x_1, y_1, mbfl):
    y_intercept_bfl = y_1 - (mbfl * x_1)
    return y_intercept_bfl

def f_y_intercept_wfl(x_1, y_1, mwfl):
    y_intercept_wfl = y_1 - (mwfl * x_1)
    return y_intercept_wfl

def f_dy_intercept(y_intercept_bfl, y_intercept_wfl):
    dy_intercept = abs(y_intercept_bfl - y_intercept_wfl)
    return dy_intercept
