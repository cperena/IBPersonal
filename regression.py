def deri(times):
    coeff = int(input("Enter the coefficient of the term: \n"))
    exp = int(input("Enter the exponent of the term: \n"))
    t = []
    for n in range (times):
        if coeff < 0 and exp < 0:
            coeff = (coeff*exp)
            exp = (exp-1)
            t.append(str(coeff) + " * x^" + str(n) + "x^" + str(exp) + " / " + str(n) + ("!") + " +")
        elif exp > 1:
            coeff = coeff*exp
            exp = exp-1
            t.append((str(coeff) + "x^" + str(exp) + " * x^" + str(n) + " / " + str(n) + ("!") + " +"))
        elif exp == 1:
            coeff = coeff
            exp = 0
            t.append((str(coeff) + " * x^" + str(n) + " / " + str(n) + ("!") +  " +"))
        elif exp == 0:
            coeff = 0
            exp = 0
            t.append(str(0) + " * x^" + str(n) + " / " + str(n) + ("!") + " +")
        elif coeff < 0:
            coeff = (coeff*exp)
            exp = (exp-1)
            t.append((str(coeff*exp) + "x^" + str(exp) + " * x^" + str(n) + " / " + str(n) + ("!") + " +"))
        elif coeff == 0:
            coeff = 0
            exp = 0
            t.append((str(0) + " * x^" + str(n) + " / " + str(n) + ("!")  + " +" ))
        elif exp < 0:
            coeff = (coeff*exp)
            exp = (exp-1)
            t.append((str(coeff*exp) +  "x^" + str(exp) + " * x^" + str(n) + " / " + str(n) + ("!")  + " +"))
    return t

answer = str(deri(int(input("\n How many derivates do you want? \n"))))
print ("\n" + str(answer))
