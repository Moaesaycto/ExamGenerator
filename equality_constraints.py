import random
from options import *
import numpy as np

def generate():
    try:
        q_type = random.randint(0, 3)
        if q_type == 0: equation, constraints, point = two_var_lin()
        elif q_type == 1: equation, constraints, point = two_var_circ()
        elif q_type == 2: equation, constraints, point = three_var_lin_circ()
        else: equation, constraints, point = three_var_lin_lin()

        n = len(constraints)
        question = r"Consider function $f : \mathbb{R}^" + str(n) + r" \mapsto \mathbb{R}$ given by $$f(\boldsymbol{x}) =" + equation + r",$$"
        if n == 2: question += r"where $\boldsymbol{x} = (x_1, x_2)$ and is subject to the constraint $" + constraints[0] + r".$"
        else: question += r"where $\boldsymbol{x} = (x_1, x_2, x_3) and is subject to the constraints $" + constraints[0] + r"$ and $" + constraints[1] + r".$"
        
        question += r" Now consider the point $\boldsymbol{x}^* = " + point + r"^T$. Show that this point is a regular point and that it satisfies the first order necessary conditions."
        question += r" Also verify that $\boldsymbol{x}^*$ satisfies the second order sufficient conditions for a local minimiser of the problem. Is $\boldsymbol{x}^*$ a global minimiser?"
        return {'question': question, 'answer': "Unavailable"}
    except: return generate()


def two_var_lin():
    a, b, c, d, e = 0.0, 0.0, 0, 0, 0
    const_valid = False
    while ([a, b, c, d, e].count(0) > MIN_NUM_OF_TERMS_EQ and [a, b, c, d, e].count(0) < MAX_NUM_OF_TERMS_EQ) or (
        not a.is_integer() or not b.is_integer()) or not const_valid or a < 0 or b < 0 or c < 0:
        l = random.randint(-2, 2)*2
        while l == 0: l = random.randint(-2, 2)*2
        ca = np.array([random.randint(-4, 4) for _ in range(2)])
        while ca[0] == 0 or ca[1] == 0: ca = np.array([random.randint(-4, 4) for _ in range(2)])
        x_star = np.array([random.choice([-1, 1, 0.5, -0.5]) for _ in range(2)])

        a, b, c, d, e = 0.0, 0.0, 0, 0, 0
        const_valid = False
        c, d, e = random.randint(-2, 2)*2, random.randint(-2, 2)*2, random.randint(-2, 2)*2
        a = (-l*ca[0] - c*x_star[1] - d)/(2 * x_star[0])
        b = (-l*ca[1] - c*x_star[0] - e)/(2 * x_star[1])

        const = float(-ca[0]*x_star[0] - ca[1]*x_star[1])
        if const.is_integer(): const_valid = True

    equation = abcde_eq(a, b, c, d, e)

    constraint = ""
    if ca[0] == 1: constraint += "x_1"
    elif ca[0] == -1: constraint += "-x_1"
    elif ca[0] != 0: constraint += str(ca[0]) + "x_1"

    if ca[1] == 1: constraint += "+x_2"
    elif ca[1] == -1: constraint += "-x_2"
    elif ca[1] != 0: constraint += "+" + str(ca[1]) + "x_2"

    if const > 0: constraint += "+" + str(int(const))
    elif const < 0: constraint += str((const))

    constraint += "= 0"

    point = "\left["
    if x_star[0] == 0.5: point += r"\dfrac{1}{2}"
    elif x_star[0] == -0.5: point += r"- \dfrac{1}{2}"
    else: point += str(int(x_star[0]))
    point += ", "
    if x_star[1] == 0.5: point += r"\dfrac{1}{2}"
    elif x_star[1] == -0.5: point += r"- \dfrac{1}{2}"
    else: point += str(int(x_star[1]))
    point += r"\right]"

    return equation, [constraint], point


def two_var_circ():
    a, b, c, d, e = 0.0, 0.0, 0, 0, 0
    const_valid = False
    while [a, b, c, d, e].count(0) > MIN_NUM_OF_TERMS_EQ or (not a.is_integer() or not b.is_integer()) or not const_valid or a < 0 or b < 0 or c < 0:
        l = random.randint(-2, 2)
        while l == 0: l = random.randint(-2, 2)
        h1, h2 = random.randint(-2, 2), random.randint(-2, 2)
        x_star = [0, 0]
        while x_star[0] == 0 or x_star[1] == 0:
            m, n = random.randint(1, 5), random.randint(1, 5)
            x_star = random.choice([[h1 + abs(m**2 - n**2), h2 + 2*m*n], [h1 + 2*m*n, h2 + abs(m**2 - n**2)]])
        ca = [2*(x_star[0] - h1), 2*(x_star[1] - h2)]

        a, b, c, d, e = 0.0, 0.0, 0, 0, 0
        const_valid = False
        c, d, e = random.randint(-2, 2)*2, random.randint(-2, 2)*2, random.randint(-2, 2)*2
        a = (-l*ca[0] - c*x_star[1] - d)/(2 * x_star[0])
        b = (-l*ca[1] - c*x_star[0] - e)/(2 * x_star[1])

        const = float(-ca[0]*x_star[0] - ca[1]*x_star[1])
        if const.is_integer(): const_valid = True

    equation = abcde_eq(a, b, c, d, e)

    constraint = ""
    if h1 == 0: constraint += "x_1^2"
    if h1 > 0: constraint += "(x_1-" + str(int(h1)) + ")^2"
    if h1 < 0: constraint += "(x_1+" + str(int(abs(h1))) + ")^2"

    if h2 == 0: constraint += "+x_2^2"
    if h2 > 0: constraint += "+(x_2-" + str(int(h2)) + ")^2"
    if h2 < 0: constraint += "+(x_2+" + str(int(abs(h2))) + ")^2"
    constraint += "=" + str(int((x_star[0] - h1)**2 + (x_star[1] - h2)**2))

    point = r"\left[" + str(int(x_star[0])) + ", " + str(int(x_star[1])) + r"\right]"
    return equation, [constraint], point


def abcde_eq(a, b, c, d, e):
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


def three_var_lin_lin():
    a1, a2, a3, b1, b2, b3, c1, c2, c3 = 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0
    const_valid = False
    while ([a1, a2, a3, b1, b2, b3, c1, c2, c3].count(0) > MIN_NUM_OF_TERMS_EQ and [a1, a2, a3, b1, b2, b3, c1, c2, c3].count(0) < MAX_NUM_OF_TERMS_EQ) or (
        not a1.is_integer() or not a2.is_integer() or not a3.is_integer()) or not const_valid or a1 < 0 or a2 < 0 or a3 < 0 or b1 < 0 or b2 < 0 or b3 < 0:
        l1, l2 = random.randint(-2, 2)*2, random.randint(-2, 2)*2
        while l1 == 0: l1 = random.randint(-2, 2)*2
        while l2 == 0: l2 = random.randint(-2, 2)*2
        ca1 = [0, 0, 0]
        while ca1[0] == 0 or ca1[1] == 0 or ca1[2] == 0: ca1 = [random.randint(-4, 4) for _ in range(3)]
        ca2 = [0, 0, 0]
        while ca2[0] == 0 or ca2[1] == 0 or ca2[2] == 0: ca2 = [random.randint(-4, 4) for _ in range(3)]
        x_star = np.array([random.choice([-1, 1, 0.5, -0.5]) for _ in range(3)])

        a1, a2, a3, b1, b2, b3, c1, c2, c3 = 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0
        const_valid = False
        b1, b2, b3, c1, c2, c3 = random.randint(-2, 2)*2, random.randint(-2, 2)*2, random.randint(-2, 2)*2, random.randint(-2, 2)*2, random.randint(-2, 2)*2, random.randint(-2, 2)*2
        a1 = (-l1*ca1[0] - l2*ca2[0] - b1*x_star[1] - b2*x_star[2] - c1)/(2 * x_star[0])
        a2 = (-l1*ca1[1] - l2*ca2[1] - b1*x_star[0] - b3*x_star[2] - c2)/(2 * x_star[1])
        a3 = (-l1*ca1[2] - l2*ca2[2] - b2*x_star[0] - b3*x_star[1] - c3)/(2 * x_star[2])

        const1 = float(-ca1[0]*x_star[0] - ca1[1]*x_star[1] - ca1[2]*x_star[2])
        const2 = float(-ca2[0]*x_star[0] - ca2[1]*x_star[1] - ca2[2]*x_star[2])
        if const2.is_integer() and const1.is_integer(): const_valid = True

    equation = a1a2a3b1b2b3c1c2c3c3(a1, a2, a3, b1, b2, b3, c1, c2, c3)

    constraint1 = ""
    if ca1[0] == 1: constraint1 += "x_1"
    elif ca1[0] == -1: constraint1 += "-x_1"
    elif ca1[0] > 0: constraint1 += "+" + str(int(ca1[0])) + "x_1"
    elif ca1[0] < 0: constraint1 += str(int(ca1[0])) + "x_1"

    if ca1[1] == 1: constraint1 += "+x_2"
    elif ca1[1] == -1: constraint1 += "-x_2"
    elif ca1[1] > 0: constraint1 += "+" + str(int(ca1[1])) + "x_2"
    elif ca1[1] < 0: constraint1 += str(int(ca1[1])) + "x_2"

    if ca1[2] == 1: constraint1 += "+x_3"
    elif ca1[2] == -1: constraint1 += "-x_3"
    elif ca1[2] > 0: constraint1 += "+" + str(int(ca1[2])) + "x_3"
    elif ca1[2] < 0: constraint1 += str(int(ca1[2])) + "x_3"

    if const1 > 0: constraint1 += "+" + str(int(const1))
    elif const1 < 0: constraint1 += str(int(const1))
    constraint1 += "=0"
    if constraint1[0] == "+": constraint1 = constraint1[1:]

    constraint2 = ""
    if ca2[0] == 1: constraint2 += "x_1"
    elif ca2[0] == -1: constraint2 += "-x_1"
    elif ca2[0] > 0: constraint2 += "+" + str(int(ca2[0])) + "x_1"
    elif ca2[0] < 0: constraint2 += str(int(ca2[0])) + "x_1"

    if ca2[1] == 1: constraint2 += "+x_2"
    elif ca2[1] == -1: constraint2 += "-x_2"
    elif ca2[1] > 0: constraint2 += "+" + str(int(ca2[1])) + "x_2"
    elif ca2[1] < 0: constraint2 += str(int(ca2[1])) + "x_2"

    if ca2[2] == 1: constraint2 += "+x_3"
    elif ca2[2] == -1: constraint2 += "-x_3"
    elif ca2[2] > 0: constraint2 += "+" + str(int(ca2[2])) + "x_3"
    elif ca2[2] < 0: constraint2 += str(int(ca2[2])) + "x_3"

    if const2 > 0: constraint2 += "+" + str(int(const2))
    elif const2 < 0: constraint2 += str(int(const2))

    constraint2 += "=0"
    if constraint2[0] == "+": constraint2 = constraint2[1:]

    point = "\left["
    if x_star[0] == 0.5: point += r"\dfrac{1}{2}"
    elif x_star[0] == -0.5: point += r"- \dfrac{1}{2}"
    else: point += str(int(x_star[0]))
    point += ", "
    if x_star[1] == 0.5: point += r"\dfrac{1}{2}"
    elif x_star[1] == -0.5: point += r"- \dfrac{1}{2}"
    else: point += str(int(x_star[1]))
    point += ", "
    if x_star[2] == 0.5: point += r"\dfrac{1}{2}"
    elif x_star[2] == -0.5: point += r"- \dfrac{1}{2}"
    else: point += str(int(x_star[2]))
    point += r"\right]"

    return equation, [constraint1, constraint2], point


def a1a2a3b1b2b3c1c2c3c3(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    equation = ""
    if a1 == 1: equation += "x_1^2"
    elif a1 == -1: equation += "-x_1^2"
    elif a1 > 0: equation += "+" + str(int(a1)) + "x_1^2"
    elif a1 < 0: equation += str(int(a1)) + "x_1^2"

    if a2 == 1: equation += "+x_2^2"
    elif a2 == -1: equation += "-x_2^2"
    elif a2 > 0: equation += "+" + str(int(a2)) + "x_2^2"
    elif a2 < 0: equation += str(int(a2)) + "x_2^2"

    if a3 == 1: equation += "+x_3^2"
    elif a3 == -1: equation += "-x_3^2"
    elif a3 > 0: equation += "+" + str(int(a3)) + "x_3^2"
    elif a3 < 0: equation += str(int(a3)) + "x_3^2"

    if b1 == 1: equation += "+x_1x_2"
    elif b1 == -1: equation += "-x_1x_2"
    elif b1 > 0: equation += "+" + str(int(b1)) + "x_1x_2"
    elif b1 < 0: equation += str(int(b1)) + "x_1x_2"

    if b2 == 1: equation += "+x_1x_3"
    elif b2 == -1: equation += "-x_1x_3"
    elif b2 > 0: equation += "+" + str(int(b2)) + "x_1x_3"
    elif b2 < 0: equation += str(int(b2)) + "x_1x_3"

    if b3 == 1: equation += "+x_2x_3"
    elif b3 == -1: equation += "-x_2x_3"
    elif b3 > 0: equation += "+" + str(int(b3)) + "x_2x_3"
    elif b3 < 0: equation += str(int(b3)) + "x_2x_3"

    if c1 == 1: equation += "+x_1"
    elif c1 == -1: equation += "-x_1"
    elif c1 > 0: equation += "+" + str(int(c1)) + "x_1"
    elif c1 < 0: equation += str(int(c1)) + "x_1"

    if c2 == 1: equation += "+x_2"
    elif c2 == -1: equation += "-x_2"
    elif c2 > 0: equation += "+" + str(int(c2)) + "x_2"
    elif c2 < 0: equation += str(int(c2)) + "x_2"

    if c3 == 1: equation += "+x_3"
    elif c3 == -1: equation += "-x_3"
    elif c3 > 0: equation += "+" + str(int(c3)) + "x_3"
    elif c3 < 0: equation += str(int(c3)) + "x_3"

    if equation[0] == "+": equation = equation[1:]
    return equation


def three_var_lin_circ():
    a1, a2, a3, b1, b2, b3, c1, c2, c3 = 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0
    const_valid = False
    while ([a1, a2, a3, b1, b2, b3, c1, c2, c3].count(0) > MIN_NUM_OF_TERMS_EQ and [a1, a2, a3, b1, b2, b3, c1, c2, c3].count(0) < MAX_NUM_OF_TERMS_EQ) or (
        not a1.is_integer() or not a2.is_integer() or not a3.is_integer()) or not const_valid or a1 < 0 or a2 < 0 or a3 < 0 or b1 < 0 or b2 < 0 or b3 < 0:
        l1, l2 = random.randint(-2, 2)*2, random.randint(-2, 2)*2
        while l1 == 0: l1 = random.randint(-4, 4)
        while l2 == 0: l2 = random.randint(-4, 4)
        ca1 = [0, 0, 0]
        while ca1[0] == 0 or ca1[1] == 0 or ca1[2] == 0: ca1 = [random.randint(-4, 4) for _ in range(3)]
        x_star = np.array([random.choice([-1, 1, -1/2, 1/2]) for _ in range(3)])
        h1, h2, h3 = random.randint(-2, 2), random.randint(-2, 2), random.randint(-2, 2)
        ca2 = [2*(x_star[0] - h1), 2*(x_star[1] - h2), 2*(x_star[2] - h3)]
        const1 = float(-ca1[0]*x_star[0] - ca1[1]*x_star[1] - ca1[2]*x_star[2])
        R = (x_star[0] - h1)**2 + (x_star[1] - h2)**2 + (x_star[2] - h3)**2

        a1, a2, a3, b1, b2, b3, c1, c2, c3 = 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0
        const_valid = False
        b1, b2, b3, c1, c2, c3 = random.randint(-2, 2)*2, random.randint(-2, 2)*2, random.randint(-2, 2)*2, random.randint(-2, 2)*2, random.randint(-2, 2)*2, random.randint(-2, 2)*2
        a1 = (-l1*ca1[0] - l2*ca2[0] - b1*x_star[1] - b2*x_star[2] - c1)/(2 * x_star[0])
        a2 = (-l1*ca1[1] - l2*ca2[1] - b1*x_star[0] - b3*x_star[2] - c2)/(2 * x_star[1])
        a3 = (-l1*ca1[2] - l2*ca2[2] - b2*x_star[0] - b3*x_star[1] - c3)/(2 * x_star[2])

        if const1.is_integer(): const_valid = True

    equation = a1a2a3b1b2b3c1c2c3c3(a1, a2, a3, b1, b2, b3, c1, c2, c3)

    constraint1 = ""
    if ca1[0] == 1: constraint1 += "x_1"
    elif ca1[0] == -1: constraint1 += "-x_1"
    elif ca1[0] > 0: constraint1 += "+" + str(int(ca1[0])) + "x_1"
    elif ca1[0] < 0: constraint1 += str(int(ca1[0])) + "x_1"

    if ca1[1] == 1: constraint1 += "+x_2"
    elif ca1[1] == -1: constraint1 += "-x_2"
    elif ca1[1] > 0: constraint1 += "+" + str(int(ca1[1])) + "x_2"
    elif ca1[1] < 0: constraint1 += str(int(ca1[1])) + "x_2"

    if ca1[2] == 1: constraint1 += "+x_3"
    elif ca1[2] == -1: constraint1 += "-x_3"
    elif ca1[2] > 0: constraint1 += "+" + str(int(ca1[2])) + "x_3"
    elif ca1[2] < 0: constraint1 += str(int(ca1[2])) + "x_3"

    if const1 > 0: constraint1 += "+" + str(int(const1))
    elif const1 < 0: constraint1 += str(int(const1))
    constraint1 += "=0"
    if constraint1[0] == "+": constraint1 = constraint1[1:]

    constraint2 = ""
    if h1 == 0: constraint2 += "x_1^2"
    if h1 > 0: constraint2 += "(x_1-" + str(int(h1)) + ")^2"
    if h1 < 0: constraint2 += "(x_1+" + str(int(abs(h1))) + ")^2"

    if h2 == 0: constraint2 += "+x_2^2"
    if h2 > 0: constraint2 += "+(x_2-" + str(int(h2)) + ")^2"
    if h2 < 0: constraint2 += "+(x_2+" + str(int(abs(h2))) + ")^2"

    if h3 == 0: constraint2 += "+x_3^2"
    if h3 > 0: constraint2 += "+(x_3-" + str(int(h3)) + ")^2"
    if h3 < 0: constraint2 += "+(x_3+" + str(int(abs(h3))) + ")^2"
    constraint2 += "=" + str(int(R))

    point = "\left["
    if x_star[0] == 0.5: point += r"\dfrac{1}{2}"
    elif x_star[0] == -0.5: point += r"- \dfrac{1}{2}"
    else: point += str(int(x_star[0]))
    point += ", "
    if x_star[1] == 0.5: point += r"\dfrac{1}{2}"
    elif x_star[1] == -0.5: point += r"- \dfrac{1}{2}"
    else: point += str(int(x_star[1]))
    point += ", "
    if x_star[2] == 0.5: point += r"\dfrac{1}{2}"
    elif x_star[2] == -0.5: point += r"- \dfrac{1}{2}"
    else: point += str(int(x_star[2]))
    point += r"\right]"
    return equation, [constraint1, constraint2], point
