import random
from options import *

def generate():
    FUNC_DIM = random.randint(2, MAX_FUNC_DIM)
    num_of_terms = random.randint(MIN_NUM_OF_TERMS, MAX_NUM_OF_TERMS)
    term_list = [[random.randint(0, FUNC_DIM) for _ in range(FUNC_DIM)] for _ in range(num_of_terms)]
    for term in term_list: term.sort()
    
    equation = "f("
    for i in range(FUNC_DIM): equation += "x_" + str(i + 1) + ",~"
    equation = equation[:-2] + ")="

    first = True
    for term in term_list:
        coeff = random.randint(-12, 12)
        if coeff == 0: coeff = 1
        if coeff < 0: equation += "-"
        elif not first: equation += "+"
        if abs(coeff) != 1: equation += str(abs(coeff))

        if first: first = False

        for i in range(FUNC_DIM):
            mult = term.count(i)
            if mult == 0: continue
            elif mult == 1: equation += "x_" + str(i + 1)
            else: equation += "x_" + str(i + 1) + "^" + str(mult)

    return {'question': r"Consider the function $f: \mathbb{R}^" + str(FUNC_DIM) + r"\mapsto \mathbb{R}$, where $$" + equation + r".$$ Find and classify all stationary point of this function.", 'answer': "Unavailable"}

if __name__ == '__main__':
    print(generate())