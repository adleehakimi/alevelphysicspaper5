def f_gradient_bfl(x_1, y_1, x_2, y_2):
    gradient_bfl = (y_2 - y_1) / (x_2 - x_1)
    return gradient_bfl

def f_gradient_wfl(x_3, y_3, x_4, y_4):
    gradient_wfl = (y_3 - y_4) / (x_3 - x_4)
    return gradient_wfl

def f_gradient_change(gradient_bfl, gradient_wfl):
    gradient_change = abs(gradient_bfl - gradient_wfl)
    return gradient_change