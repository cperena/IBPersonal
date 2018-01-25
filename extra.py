if coeff < 0 and exp < 0:
        print("The derivate is: " + str(abs(coeff*exp)) + "/(x^" + str(abs(exp-1)) + ")")
    elif exp > 1:
        print("The derivate is: " + str(coeff*exp) + "x^" + str(exp-1))
    elif exp == 1:
        print("The derivate is: " + str(coeff))
    elif exp == 0:
        print("The derivate is: 0")
    elif coeff < 0:
        print("The derivate is: " + str(coeff*exp) + "x^" + str(exp-1))
    elif coeff == 0:
        print("The derivate is: 0")
    elif exp < 0:
        print("The derivate is: " + str(coeff*exp) + "/(x^" + str(abs(exp-1)) + ")")
