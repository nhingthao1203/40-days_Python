import math
def quadratic_equation(a,b,c):
    denta = b**2-4*a*c
    if denta > 0:
        x1 = (-b+ math.sqrt(denta))/(2*a)
        x2 = (-b- math.sqrt(denta))/(2*a)
        return x1,x2
    elif denta == 0:
        return -b/(2*a)
    else:
        return "phương trình vô nghiệm"
    
print(quadratic_equation(a=2,b=6,c=4))
print(quadratic_equation(a=1,b=2,c=1))
print(quadratic_equation(a=4,b=6,c=3))
