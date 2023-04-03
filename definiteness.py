import numpy as np
from options import *

def generate():
    length = np.random.randint(2, MAX_DIM + 1)
    eigenvalues = np.random.randint(-MAX_EIGENVALUE_MOD, MAX_EIGENVALUE_MOD, size=length)
    eigenvectors = np.random.randint(-MAX_EIGENVECTOR_COMP_MOD, MAX_EIGENVECTOR_COMP_MOD, size=(length, length))
    S = np.matrix(eigenvectors)
    L = np.diag(eigenvalues)
    try: A = np.linalg.det(S) * S * L * S.I
    except: return generate()

    for i in range(length):
        for j in range(length):
            if abs(A[i, j]) < 1e-5: return generate()

    A = A.tolist()
    q_set = {}
    q = "Consider the matrix $$A =" + "\\begin{pmatrix}"
    for row in A:
        for i in row: q += str(round(i, 0))[:-2] + "&"
        q = q[:-1] + "\\\\"
    q_set['question'] = q[:-2] + """\\end{pmatrix}.$$""" + """ State whether this matrix is positive definite, negative definite, positive semi-definite, negative semi-definite, or indefinite."""
    q_set['answer'] = get_matrix_definiteness(eigenvalues)
    return q_set

def get_matrix_definiteness(eigenvalues):
        if np.all(eigenvalues) > 0: return "Positive definite"
        elif np.all(eigenvalues < 0): return "Negative definite"
        elif np.all(eigenvalues >= 0): return "Positive semi-definite"
        elif np.all(eigenvalues <= 0): return "Negative semi-definite"
        else: return "Indefinite"

if __name__ == '__main__':
    question = generate()
    print(question['question'])