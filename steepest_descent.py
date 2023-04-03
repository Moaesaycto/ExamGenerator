import numpy as np
from numpy import linalg as LA
from random import randint

def is_pos_def(x):
    """check if a matrix is symmetric positive definite"""
    return np.all(np.linalg.eigvals(x) > 0)

def steepest_descent(A, b, x):
    """
    Solve Ax = b
    Parameter x: initial values
    """
    if (is_pos_def(A) == False) | (A != A.T).any():
        raise ValueError('Matrix A needs to be symmetric positive definite (SPD)')
    r = b - A @ x
    k = 0
    while LA.norm(r) > 1e-10 :
        p = r
        q = A @ p
        alpha = (p @ r) / (p @ q)
        x = x + alpha * p
        r = r - alpha * q
        k =+ 1

    return x


def steepest_descent_det(A, b, x, minx):
    init_x = x
    """
    Solve Ax = b
    Parameter x: initial values
    """
    if (is_pos_def(A) == False) | (A != A.T).any():
        raise ValueError('Matrix A needs to be symmetric positive definite (SPD)')
    r = b - A @ x
    k = 0
    x_rat, y_rat = [], []
    while LA.norm(r) > 1e-10 :
        p = r
        q = A @ p
        alpha = (p @ r) / (p @ q)
        x_prev = x
        x = x + alpha * p
        x_curr = x

        x_rat.append((x_curr[0] - minx[0])/(x_prev[0] - minx[0])) 
        y_rat.append((x_curr[1] - minx[1])/(x_prev[1] - minx[1]))
        r = r - alpha * q
        k =+ 1

    x_ratio, y_ratio = np.mean(x_rat[:3]), np.mean(y_rat[:3])
    
    x = init_x
    r = b - A @ x
    
    p = r
    q = A @ p
    alpha = (p @ r) / (p @ q)
    x_prev = x
    x = x + alpha * p
    x_curr = x
    nx, ny = (x_curr[0] - minx[0])/x_ratio, (x_curr[1] - minx[1])/y_ratio

    return [get_frac(x_rat[0]), get_frac(y_rat[0]), -round(nx,0), -round(ny,0)]


def get_frac(frac):
    abfrac = abs(frac)
    ACCURACY = 1e-5
    MAX_N = 100
    for n in range(1, MAX_N):
        for d in range(1, MAX_N):
            if abs(abfrac - n/d) < ACCURACY:
                return (frac/abfrac*n, d)

    return None


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


def latex_frac(frac):
    frac = get_frac(frac)
    if frac == None: return None
    if frac[0] == frac[1]: return "1"
    elif frac[1] == 1: return str(int(frac[0]))
    elif frac[0] == 0: return "0"
    elif frac[0] % frac[1] == 0: return str(int(frac[0]/frac[1]))
    else:
        if frac[0] < 0: equation = r"-"
        else: equation = "+"
        equation += r"\dfrac{" + str(int(abs(frac[0]))) + r"}{" + str(int(frac[1])) + r"}"
        return equation


def induction(xcoef, xrat, xmin, ycoef, yrat, ymin):
    equation = r"\left("
    if xcoef == 1: pass
    elif xcoef == -1: equation += r"-"
    else: equation += str(int(round(xcoef, 0)))

    if xrat[0] == xrat[1]: pass
    elif xrat[1] == 1: equation += r"(" + str(int(xrat[0])) + r")^k"
    else:
        equation += r"\left(\dfrac{"
        if xrat[0] < 0: equation += r"-"
        equation += str(abs(int(xrat[0]))) + r"}{" + str(abs(xrat[1])) + r"}\right)^k"
    if xmin == 0: pass
    else: equation += latex_frac(xmin)
    equation += r",~"

    if ycoef == 1: pass
    elif ycoef == -1: equation += r"-"
    else: equation += str(int(round(ycoef, 0)))


    if yrat[0] == yrat[1]: pass
    elif yrat[1] == 1: equation += r"(" + str(int(round(yrat[0], 0))) + r")^k"
    else:
        equation += r"\left("
        if yrat[0] < 0: equation += r"-"
        equation += r"\dfrac{" + str(abs(int(yrat[0]))) + r"}{" + str(abs(yrat[1])) + r"}\right)^k"
    
    if ymin == 0: pass
    else: equation += latex_frac(ymin)
    equation += r"\right)"

    return equation


def generate_pars():
    try:
        A = np.array([[randint(1, 4), 0], [0, randint(1, 4)]])
        b = np.random.randint(-4, 4, size=2)
        x0 = [0, 0]

        minx = steepest_descent(A, b, x0)
        result = steepest_descent_det(A, b, x0, minx)
        equation = abcde_eq(A[0][0], A[1][1], 0, -b[0], -b[1])
        if result[2] == 0 or result[3] == 0: return generate_pars()
        if result[0][1] > 5 or result[1][1] > 5: return generate_pars()
        inductions = induction(result[2], result[0], -minx[0]/2, result[3], result[1], -minx[1]/2)
        return equation, inductions
    except:
        return generate_pars()
    

def generate():
    equation, inductions = generate_pars()
    q = r"Consider the function: $$f(x_1, x_2) = " + equation + r".$$"
    q += r"Prove by induction that the method of steepest descent applied with an initial guess $\boldsymbol{x}^{(1)} = \boldsymbol{0}$ generates the sequence $\{\boldsymbol{x}^{(k)}\}$ where $$\{\boldsymbol{x}^{(k + 1)}\} = "
    q += inductions + r".$$ Hence, deduce the minimiser."

    return {
        "question": q,
        "answer": r"Unavailable"
    }


if __name__=='__main__':
    gen = generate_pars()
    print(gen[0], gen[1])
