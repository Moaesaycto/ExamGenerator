import random
from options import *

def generate():
    problem_type = random.randint(1, 7)
    if problem_type == 1: equation, constraints, point = lin_lin()
    elif problem_type == 2: equation, constraints, point = lin_x1()
    elif problem_type == 3: equation, constraints, point = lin_x2()
    elif problem_type == 4: equation, constraints, point = lin_linx1()
    elif problem_type == 5: equation, constraints, point = lin_linx2()
    elif problem_type == 6: equation, constraints, point = circ()
    elif problem_type == 7: equation, constraints, point = circ_lin()

    q = "Consider the function $f: \mathbb{R}^2\mapsto \mathbb{R}$, where $$f(x_1, x_2)=" + equation + ",$$ subject to the constraint"
    if len(constraints) == 1: q += " $" + constraints[0] + "$"
    if len(constraints) == 2: q += "s $" + constraints[0] + "$ and $" + constraints[1] + "$"
    if len(constraints) == 3: q += "s $" + constraints[0] + "$, $" + constraints[1] + "$ and $" + constraints[2] + "$"

    q += r""". We aim to minimise this function in the given region defined by the constraints. Sketch the region and confirm whether or not this is a convex optimisation problem. If it is, write down the Kuhn-Tucker conditions for this problem and show that $\boldsymbol{x}^*=""" + point + r"""^T$ satisfies them. Is $\boldsymbol{x}^*$ a global minimum?"""
    
    return {'question': q, 'answer': "Unavailable"}


def lin_lin():
    a, b, c, d, e = 0.0, 0.0, 0, 0, 0
    const_valid = False
    while [a, b, c, d, e].count(0) > MIN_NUM_OF_TERMS_EQ or (not a.is_integer() or not b.is_integer()) or not const_valid or a < 0 or b < 0 or c < 0 or (a == 0 and b == 0 and c == 0):
        l = random.randint(-2, 2)*2
        while l == 0: l = random.randint(-2, 2)*2
        x_star = [random.choice([1, -1, 0.5, -0.5]), random.choice([1, -1, 0.5, -0.5])]
        m, n = random.randint(-3, 3), random.randint(-3, 3)
        while m == 0 or n == 0: m, n = random.randint(-3, 3), random.randint(-3, 3)
    
        a, b, c, d, e = 0.0, 0.0, 0, 0, 0
        const_valid = False
        c, d, e = random.randint(-2, 2)*2, random.randint(-2, 2)*2, random.randint(-2, 2)*2
        a = (-l*m - c*x_star[1] - d)/(2 * x_star[0])
        b = (l*n - c*x_star[0] - e)/(2 * x_star[1])

        const = float(n*x_star[0] - m*x_star[1])
        if const.is_integer(): const_valid = True

    constraints = [linear_eq(m, -n, const)]
    constraints += random.sample([r"x_1 \geq 0", r"x_2\geq 0"], random.randint(0, 2))
    return abcde_eq(a, b, c, d, e), constraints, point_latex(x_star)


def lin_x1():
    a, b, c, d, e = 0.0, 0.0, 0, 0, 0
    while [a, b, c, d, e].count(0) > MIN_NUM_OF_TERMS_EQ or not b.is_integer() or a < 0 or b < 0 or c < 0 or (b == 0 and c == 0 and e == 0) or l == 0:
        x2 = random.randint(-4, 4)
        while x2 == 0: x2 = random.randint(-4, 4)
        x_star = [0, x2]
    
        a, b, d, e = 0.0, 0.0, 0, 0,
        c, d, e = random.randint(-2, 2)*2, random.randint(-2, 2)*2, random.randint(-2, 2)*2
        a = random.randint(-4, 4)
        while a == 0: a = random.randint(-4, 4)
        b = - e/(2*x_star[1])
        l = c*x_star[1] + d

        m, n, const = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
        while not n*x_star[1] + const < 0 or m == 0 or n == 0 or const == 0: m, n, const = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)

    constraints = [linear_eq(m, n, const), "x_1 \geq 0"]
    constraints += random.sample([r"x_2\geq 0"], random.randint(0, 1))
    return abcde_eq(a, b, c, d, e), constraints, point_latex(x_star)


def lin_x2():
    a, b, c, d, e = 0.0, 0.0, 0, 0, 0
    while [a, b, c, d, e].count(0) > MIN_NUM_OF_TERMS_EQ or not a.is_integer() or a < 0 or b < 0 or c < 0 or (b == 0 and c == 0 and e == 0) or l == 0:
        x1 = random.randint(-4, 4)
        while x1 == 0: x1 = random.randint(-4, 4)
        x_star = [x1, 0]
    
        a, b, d, e = 0.0, 0.0, 0, 0,
        c, d, e = random.randint(-2, 2)*2, random.randint(-2, 2)*2, random.randint(-2, 2)*2
        b = random.randint(-4, 4)
        while b == 0: b = random.randint(-4, 4)
        a = - d/(2*x_star[0])
        l = c*x_star[0] + e

        m, n, const = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
        while not m*x_star[0] + const < 0 or m == 0 or n == 0 or const == 0: m, n, const = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)

    constraints = [linear_eq(m, n, const), "x_2 \geq 0"]
    constraints += random.sample([r"x_1\geq 0"], random.randint(0, 1))
    return abcde_eq(a, b, c, d, e), constraints, point_latex(x_star)


def lin_linx1():
    a, b, c, d, e = 0.0, 0.0, 0, 0, 0
    while [a, b, c, d, e].count(0) > MIN_NUM_OF_TERMS_EQ or not b.is_integer() or a < 0 or b < 0 or c < 0 or (
        b == 0 and c == 0 and e == 0) or l1 == 0 or l2 == 0 or m == 0 or n == 0:
        a, c, e = random.randint(-2, 2) * 2, random.randint(-2, 2) * 2, random.randint(-2, 2) * 2
        m, n = random.randint(-3, 3), random.randint(-3, 3)
        l1, l2 = random.randint(-3, 3)*2, random.randint(-3, 3)*2
        x2 = random.randint(-3, 3)
        while x2 == 0: x2 = random.randint(-3, 3)
        x_star = [0, x2]
        d = -2*a*x_star[0] -c * x_star[1] - l1*m + l2
        b = (-c*x_star[0] - e - l1*n) / (2 * x_star[1])

        const = -m*x_star[0] - n*x_star[1]

    constraints = [linear_eq(m, n, const), "x_1 \geq 0"]
    constraints += random.sample([r"x_2\geq 0"], random.randint(0, 1))
    return abcde_eq(a, b, c, d, e), constraints, point_latex(x_star)


def lin_linx2():
    a, b, c, d, e = 0.0, 0.0, 0, 0, 0
    while [a, b, c, d, e].count(0) > MIN_NUM_OF_TERMS_EQ or not b.is_integer() or a < 0 or b < 0 or c < 0 or (
        (a == 0 and b == 0 and c == 0) or l1 == 0 or l2 == 0 or m == 0 or n == 0):
        a, c, d = random.randint(-2, 2) * 2, random.randint(-2, 2) * 2, random.randint(-2, 2) * 2
        m, n = random.randint(-3, 3), random.randint(-3, 3)
        l1, l2 = random.randint(-3, 3)*2, random.randint(-3, 3)*2
        x1 = random.randint(-3, 3)
        while x1 == 0: x1 = random.randint(-3, 3)
        x_star = [x1, 0]
        e = c*x_star[0] - n * l1 + l2
        a = (-c*x_star[1]-d-l1*m)/(2*x_star[0])

        const = -m*x_star[0] - n*x_star[1]

    constraints = [linear_eq(m, n, const), "x_2 \geq 0"]
    constraints += random.sample([r"x_1\geq 0"], random.randint(0, 1))
    print(l1, l2)
    return abcde_eq(a, b, c, d, e), constraints, point_latex(x_star)


def circ():
    a, b, c, d, e = 0.0, 0.0, 0, 0, 0
    while [a, b, c, d, e].count(0) > MIN_NUM_OF_TERMS_EQ or not b.is_integer() or a < 0 or b < 0 or c < 0 or (
        (a == 0 and b == 0 and c == 0) or l == 0):
        c, d = random.randint(-2, 2) * 2, random.randint(-2, 2) * 2
        l = random.randint(-3, 3)
        while l == 0: l = random.randint(-3, 3)
        h1, h2 = random.randint(-2, 2), random.randint(-2, 2)
        x1 = random.randint(-3, 3)
        while x1 == 0: x1 = random.randint(-3, 3)
        x2 = random.randint(-3, 3)
        while x2 == 0: x2 = random.randint(-3, 3)
        x_star = [x1, x2]

        a = (- 2*l*(x1 - h1) - c*x2 - d)/(2*x1)
        b = (- 2*l*(x2 - h2) - c*x1 - e)/(2*x2)

    m, n = 0, 0
    while m == 0: m = random.randint(-3, 3)
    while n == 0: n = random.randint(-3, 3)

    const = random.randint(-3, 3)
    while m*x_star[0] + n*x_star[1] + const == 0: const = random.randint(-3, 3)

    constraints = [circ_eq(h1, h2, (x1 - h1)**2 + (x2 - h2)**2)] + random.sample([linear_eq(m, n, const)], random.randint(0, 1))

    return abcde_eq(a, b, c, d, e), constraints, point_latex(x_star)


def circ_lin():
    a, b, c, d, e = 0.0, 0.0, 0, 0, 0
    while [a, b, c, d, e].count(0) > MIN_NUM_OF_TERMS_EQ or not b.is_integer() or a < 0 or b < 0 or c < 0 or (
        (a == 0 and b == 0 and c == 0)):
        c, d = random.randint(-2, 2) * 2, random.randint(-2, 2) * 2
        l1 = random.randint(-3, 3)
        while l1 == 0: l1 = random.randint(-3, 3)
        l2 = random.randint(-3, 3)
        while l2 == 0: l2 = random.randint(-3, 3)
        h1, h2 = random.randint(-2, 2), random.randint(-2, 2)
        x1 = random.randint(-3, 3)
        while x1 == 0 or x1 == h1: x1 = random.randint(-3, 3)
        x2 = random.randint(-3, 3)
        while x2 == 0 or x2 == h2: x2 = random.randint(-3, 3)
        x_star = [x1, x2]
        m, n, const = -(x2 - h2), x1 - h1, -x2*(x1 - h1) + x1*(x2 - h2)
    
        a = (-l2*m - 2*l1*(x1 - h1) - c*x2 - d)/(2*x1)
        b = (-l2*n - 2*l1*(x2 - h2) - c*x1 - e)/(2*x2)
        

    constraints = [circ_eq(h1, h2, (x1 - h1)**2 + (x2 - h2)**2)] + [random.choice([linear_eq(m, n, const), linear_eq(m, n, const, r'\geq')])]

    return abcde_eq(a, b, c, d, e), constraints, point_latex(x_star)


def point_latex(point):
    string = r"\left["

    if point[0] == 0.5: string += r"\frac{1}{2}"
    elif point[0] == -0.5: string += r"- \frac{1}{2}"
    else: string += str(point[0])

    string += ", "

    if point[1] == 0.5: string += r"\frac{1}{2}"
    elif point[1] == -0.5: string += r"- \frac{1}{2}"
    else: string += str(point[1])

    return string + r"\right]"


def linear_eq(A, B, C, eq=r'\leq'):
    equation = ""
    if A == 1: equation += "x_1"
    elif A == -1: equation += "-x_1"
    elif A > 0: equation += "+" + str(int(A)) + "x_1"
    elif A < 0: equation += str(int(A)) + "x_1"

    if B == 1: equation += "+x_2"
    elif B == -1: equation += "-x_2"
    elif B > 0: equation += "+" + str(int(B)) + "x_2"
    elif B < 0: equation += str(int(B)) + "x_2"

    if C == 1: equation += "+1"
    elif C == -1: equation += "-1"
    elif C > 0: equation += "+" + str(int(C))
    elif C < 0: equation += str(int(C))

    if equation[0] == "+": equation = equation[1:]
    return equation + eq + r"0"


def abcde_eq(a, b, c, d, e):
    a, b, c, d, e = int(a), int(b), int(c), int(d), int(e)
    equation = ""
    if a == 1: equation += "x_1^2"
    elif a == -1: equation += "-x_1^2"
    elif a > 0: equation += "+" + str(int(a)) + "x_1^2"
    elif a < 0: equation += str(int(a)) + "x_1^2"

    if b == 1: equation += "+x_2^2"
    elif b == -1: equation += "-x_2^2"
    elif b > 0: equation += "+" + str(int(b)) + "x_2^2"
    elif b < 0: equation += str(int(b)) + "x_2^2"

    if c == 1: equation += "+x_1x_2"
    elif c == -1: equation += "-x_1x_2"
    elif c > 0: equation += "+" + str(int(c)) + "x_1x_2"
    elif c < 0: equation += str(int(c)) + "x_1x_2"

    if d == 1: equation += "+x_1"
    elif d == -1: equation += "-x_1"
    elif d > 0: equation += "+" + str(int(d)) + "x_1"
    elif d < 0: equation += str(int(d)) + "x_1"

    if e == 1: equation += "+x_2"
    elif e == -1: equation += "-x_2"
    elif e > 0: equation += "+" + str(int(e)) + "x_2"
    elif e < 0: equation += str(int(e)) + "x_2"

    if equation[0] == "+": equation = equation[1:]
    return equation


def circ_eq(h1, h2, r2):
    equation = ""
    if h1 == 0: equation += "x_1^2"
    elif h1 > 0: equation += "(x_1 - " + str(h1) + ")^2"
    elif h1 < 0: equation += "(x_1 + " + str(-h1) + ")^2"

    if h2 == 0: equation += "+x_2^2"
    elif h2 > 0: equation += "+(x_2 - " + str(h2) + ")^2"
    elif h2 < 0: equation += "+(x_2 + " + str(-h2) + ")^2"

    return equation + r"\leq " + str(r2)
