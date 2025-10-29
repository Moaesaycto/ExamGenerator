import numpy as np
from random import randint

def is_pos_def(x):
    """check if a matrix is symmetric positive definite"""
    return np.all(np.linalg.eigvals(x) > 0)


def generate():
    A = np.random.randint(-4, 4, size=(2, 2))
    while not is_pos_def(A): A = np.random.randint(-4, 4, size=(2, 2))
    b = np.random.randint(-4, 4, size=2)
    x0 = np.random.randint(-3, 3, size=2)
    f = randint(-10, 10)

    q = r"Consider minimising the function $f: \mathbb{R}^2 \mapsto \mathbb{R}$ given by $$f(\boldsymbol{x}) = " + abcde_eq(A[0, 0], A[1, 1], A[0][1] + A[1][0], b[0], b[1], f) + r"$$ starting from $\boldsymbol{x}^{(1)} = "
    q += point_latex(x0) + r".$ Show that $f$ is a strictly convex function and find its minimiser $\boldsymbol{x}^*$ and $f(\boldsymbol{x}^*)$. Use a conjugate gradient method with the Fletcher-Reeves update to minimise $f$ starting from $\boldsymbol{x}^{(1)}$. Verify that the search directions are descent directions and that the search directions are conjugate with respect to the Hessian of $f$."

    return {
        "question": q,
        "answer": "Unavailable"
    }

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

def abcde_eq(a, b, c, d, e, f):
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

    if f == 1: equation += "+1"
    elif f == -1: equation += "-1"
    elif f > 0: equation += "+" + str(int(f))
    elif f < 0: equation += str(int(f))

    if equation[0] == "+": equation = equation[1:]
    return equation

