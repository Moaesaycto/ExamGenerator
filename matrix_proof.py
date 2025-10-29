import random

questions = [
    {
        'question': r"An $n \times n$ matrix $B$ is called idempotent if $B^2 = B$. Let $A$ be an $n \times n$ idempotent matrix. Prove that the determinant of $A$ is either $0$ or $1$.",
        'answer': r"Problem 1: https://www.math.uci.edu/~math2j/2JpracticeProofs.pdf"
    },
    {
        'question': r"""An $n \times n$ matrix $B$ is called idempotent if $B^2 = B$. Let $A$ be an $n \times n$ idempotent matrix.
                       Prove the matrix $I-A$ is also idempotent.""",
        'answer': r"Problem 2: https://www.math.uci.edu/~math2j/2JpracticeProofs.pdf"
    },
    {
        'question': r"""An $n \times n$ matrix $B$ is called nilpotent if there exists a power of the matrix $B$ which equals to the zero matrix. Let $A$ be an $n \times n$ nilpotent matrix.
                       Prove that the determinant of $A$ is $0$.""",
        'answer': r"Problem 3: https://www.math.uci.edu/~math2j/2JpracticeProofs.pdf"
    },
    {
        'question': r"""Let \(B\) be an \(n \\times n\) matrix with a positive determinant, and let \(A\) be any matrix with the same dimensions as \(B.\) Prove that the matrix $A$ is only invertible if and only if the matrix $AB$ is invertible.""",
        'answer': r"Problem 4: https://www.math.uci.edu/~math2j/2JpracticeProofs.pdf"
    },
    {
        'question': r"""Let \(\boldsymbol{v}\) be any vector of length $3$. Let\[A = (\boldsymbol{v}, 2\boldsymbol{v}, 3\boldsymbol{v}).\] Prove that $A$ is singular.""",
        'answer': r"Problem 5: https://www.math.uci.edu/~math2j/2JpracticeProofs.pdf"
    },
    {
        'question': r"""Let \(A = (\boldsymbol{a}_1, \boldsymbol{a}_2, \boldsymbol{a}_3, \boldsymbol{a}_4)\) be a \(4 \times 4\) matrix with column vectors \(\boldsymbol{a}_1\), \(\boldsymbol{a}_2\), \(\boldsymbol{a}_3\), \(\boldsymbol{a}_4.\) Suppose that \[\boldsymbol{a}_1 - 3\boldsymbol{a}_4 = \boldsymbol{0}.\] Prove that $A$ is singular.""",
        'answer': r"Problem 6: https://www.math.uci.edu/~math2j/2JpracticeProofs.pdf"
    },
    {
        'question': r"""Let $A$ be an $n \times n$ invertible matrix. Suppose that $A^{-1}= A.$ Prove that $\det{A}$ is either equal to $+1$ or $-1.$""",
        'answer': r"Problem 7: https://www.math.uci.edu/~math2j/2JpracticeProofs.pdf"
    },
    {
        'question': r"""Suppose that $A$ is an $n \times n$ matrix and that $0$ is an eigenvalue of $A.$ Prove that $A$ is not invertible.""",
        'answer': r"Problem 8: https://www.math.uci.edu/~math2j/2JpracticeProofs.pdf"
    },
    {
        'question': r"""Suppose that $A$ is an $n \times n$ matrix and that $A^2 + 3A = I.$ Prove that $A$ is invertible.""",
        'answer': r"Problem 9: https://www.math.uci.edu/~math2j/2JpracticeProofs.pdf"
    },
    {
        'question': r"""Let $A$, $B$, $C$ be $n \times n$ invertible matrices. Prove that the product $ABC$ is also invertible.""",
        'answer': r"Problem 10: https://www.math.uci.edu/~math2j/2JpracticeProofs.pdf"
    },
    {
        'question': r"""Let $A$ and $B$ be any $n \times n$ matrices. Suppose that $B$ is invertible and that $A = B^{-1}AB.$ Prove that $A$ and $B$ commute.""",
        'answer': r"Problem 11: https://www.math.uci.edu/~math2j/2JpracticeProofs.pdf"
    },
    {
        'question': r"""Let $A$ be any $n \times n$ matrix. Prove that the matrix $A + A^T$ is symmetric.""",
        'answer': r"Problem 12: https://www.math.uci.edu/~math2j/2JpracticeProofs.pdf"
    },
    {
        'question': r"""Let $A$ be any $n \times n$ matrix. Prove that the matrix $A - A^T$ is skew-symmetric.""",
        'answer': r"Problem 13: https://www.math.uci.edu/~math2j/2JpracticeProofs.pdf"
    },
    {
        'question': r"""Prove that every $n \times n$ matrix can be written as the sum of a symmetric matrix and a skew-symmetric matrix.""",
        'answer': r"Problem 14: https://www.math.uci.edu/~math2j/2JpracticeProofs.pdf"
    },
    {
        'question': r"""For any two square matrices $A$ and $B$, prove that $(AB)^2$ and $(BA)^2$ are similar if at least one of $A$ or $B$ is invertible.""",
        'answer': r"Unavailable"
    },
    {
        'question': r"""Prove that a diagonal matrix is positive definite if and only if all of its diagonal entries are positive.""",
        'answer': r"https://math.stackexchange.com/questions/211395/diagonal-matrix-proof"
    },
    {
        'question': r"""For any $n \times n$ matrix $A$, prove that $A^3 = A+I$, then $\det A > 0$.""",
        'answer': r"https://math.stackexchange.com/questions/371785/positive-definite-matrix-proof"
    },
    {
        'question': r"""Show that if $A$ is a square invertible matrix and $A^3 = A$ then $A$ is its own inverse.""",
        'answer': r"https://math.stackexchange.com/questions/1338726/invertible-matrix-proof"
    },
    {
        'question': r"""Show that if $A$ is any matrix, then $K = A^T A$ and L = $AA^T$ are both symmetric positive definite matrices.""",
        'answer': r"https://math.stackexchange.com/questions/200030/symmetric-matrix-proof"
    },
    {
        'question': r"""Let $M$ be an $n \times n$ symmetric positive definite matrix $$M = \begin{pmatrix}M_{1,1}&M_{1,2}\\M_{2,1}&M_{2,2}\end{pmatrix}$$ where $M$ is separated into blocks. Prove that $M_{2,2} - M_{2,1} M_{1,1}^{-1}M_{1,2}$ is symmetric and positive definite if $M_{1,1}$ and $M_{2,2}$ are symmetric.""",
        'answer': r"https://math.stackexchange.com/questions/4628767/positive-definite-matrix-proof-with-block-matrix"
    },
    {
        'question': r"""Consider a positive-definite matric $A$ with dimensions $n \times n$ and consider a matrix $B$ with dimensions $n \times m$. Prove that $B^T A B$ is positive definite.""",
        'answer': r"https://math.stackexchange.com/questions/1231555/positive-definite-matrix-proof-with-post"
    },
    {
        'question': r"""Suppose that $$H^+ = H - (\mathbf y^TH \mathbf y)^{-1} H\mathbf y \mathbf y^T H + (\mathbf y ^T \mathbf s )^{-1}\mathbf s \mathbf s^T$$ where $H$ is symmetric and positive definite. Suppose that $\mathbf{y}^T \mathbf{s} > 0,$ show that $H^+$ is also symmetric and positive definite.""",
        'answer': r"https://math.stackexchange.com/questions/735379/symmetric-positive-definite-matrix-proof"
    },
    {
        'question': r"""Let $A$ be an arbitrary invertible $n \times n$ matrix. Prove that there exists a positive semi-definite matrix $R$ and an orthogonal matrix $B$ such that $A = BR.$""",
        'answer': r"https://math.stackexchange.com/questions/518788/proof-that-the-product-of-a-positive-semidefinite-matrix-and-an-orthogonal-matri"
    },
    {
        'question': r"""If $A$ is positive definite, show that $A^k$ is positive definite for all $k \geq 1.$""",
        'answer': r"https://math.emory.edu/~lchen41/teaching/2020_Fall/Section_8-3.pdf"
    },
    {
        'question': r"""If $A$ and $B$ are positive definite and $r > 0$, show that $A+B$ and $r A$ are both positive definite.""",
        'answer': r"https://math.emory.edu/~lchen41/teaching/2020_Fall/Section_8-3.pdf"
    },
    {
        'question': r"""If $A$ and $B$ are positive definite, show that $\begin{pmatrix}A &0\\0&B \end{pmatrix}$ is positive definite.""",
        'answer': r"https://math.emory.edu/~lchen41/teaching/2020_Fall/Section_8-3.pdf"
    },
    {
        'question': r"""Let $A = \begin{pmatrix}1 & a\\ a&b\end{pmatrix}.$ If $a^2 < b$, show that $A$ is positive definite.""",
        'answer': r"https://math.emory.edu/~lchen41/teaching/2020_Fall/Section_8-3.pdf"
    },
    {
        'question': r"""If $A$ is an $n \times n$ positive definite matrix and $U$ is an $n \times m$ matrix of rank $m$. Show that $U^TAU$ is positive definite.""",
        'answer': r"https://math.emory.edu/~lchen41/teaching/2020_Fall/Section_8-3.pdf"
    },
    {
        'question': r"""If $A$ is positive definite, show that each diagonal entry is positive.""",
        'answer': r"https://math.emory.edu/~lchen41/teaching/2020_Fall/Section_8-3.pdf"
    },
    {
        'question': r"""Let $A_0$ be formed from $A$ by deleting rows $2$ and $4$ and deleting columns $2$ and $4$. If $A$ is positive-definite, show that $A_0$ is positive definite.""",
        'answer': r"https://math.emory.edu/~lchen41/teaching/2020_Fall/Section_8-3.pdf"
    },
    {
        'question': r"""If $A$ is positive definite, show that $A = CC^T$ where $C$ has orthogonal columns.""",
        'answer': r"https://math.emory.edu/~lchen41/teaching/2020_Fall/Section_8-3.pdf"
    },
    {
        'question': r"""If $A$ is positive definite, show that $A = C^2$ where $C$ is positive definite.""",
        'answer': r"https://math.emory.edu/~lchen41/teaching/2020_Fall/Section_8-3.pdf"
    },
    {
        'question': r"""Suppose an invertible matrix $A$ can be factored into $\mathbf{M}_{nn}$ as $A = LDU$, where $L$ is lower triangular with $1$s on the diagonal, $U$ is upper triangular with $1$s on the diagonal and $D$ is diagonal with positive diagonal entries.
                        <ol type="i">
                        <li>Show that the factorisation is unique.</li>
                        <li>Show that a matrix $A$ is positive definite if and only if $A$ is symmetric and admits a factorisation $A = LDU$ as in the previous part.</li>
                        </ol>""",
        'answer': r"https://math.emory.edu/~lchen41/teaching/2020_Fall/Section_8-3.pdf"
    },
]

def generate():
    return random.choice(questions)