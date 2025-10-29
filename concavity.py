import random

questions = [
    {
        "question": r"""Let $X$ and $Y$ represent convex regions. Show that $X \cap Y$ is also a convex region.""",
        "answer": r"http://www.athenasc.com/convexdualitysol1.pdf"
    },
    {
        "question": r"""Show that the intersection of a collection of cones is a cone.""",
        "answer": r"http://www.athenasc.com/convexdualitysol1.pdf"
    },
    {
        "question": r"""Let $C$ be a nonempty convex subset of $\mathbb{R}^n$. Let also $f = (f_1, \cdots, f_m)$, where $f_i:C \mapsto \mathbb{R}, i = 1, \cdots, m$ are convex functions, and let $g: \mathbb{R}^n \mapsto \mathbb{R}$ be a function that is convex monotonically nondecreasing over a convex set that contains the set $\{f(x)|x \in C\},$ in the sense that for all $u$, $\bar{u}$ in this set such that $u \leq \bar{u}$, we have $g(u) \leq g(\bar{u})$. Show that the function $h$ defined by $h(x) = g \circ f(x)$ is convex over $C$. If in addition, $m = 1$, $g$ is monotonically increasing and $f$ is strictly convex, then $h$ is strictly convex.""",
        "answer": r"http://www.athenasc.com/convexdualitysol1.pdf"
    },
    {
        "question": r"""If $f$ is a convex function, show that $h(x) = \alpha f(x) + \beta$ is also convex for scalars $\alpha$ and $\beta$ and $\alpha \geq 0$.""",
        "answer": r"http://www.athenasc.com/convexdualitysol1.pdf"
    },
    {
        "question": r"""If $f$ is a convex function, show that $h(x) = f(\alpha x+ \beta) $ is also convex for scalars $\alpha$ and $\beta$ and $\alpha \geq 0$.""",
        "answer": r"http://www.athenasc.com/convexdualitysol1.pdf"
    },
    {
        "question": r"""Show that the function $f(x) = \|x\|^p$ is convex when $p \geq 1$.""",
        "answer": r"http://www.athenasc.com/convexdualitysol1.pdf"
    },
    {
        "question": r"""Let $f: \mathbb{R}^n \mapsto \mathbb{R}$ be a function that is continuous over $C$, a closed convex proper subset of the domain of $f$, and let $\sigma > 0$. We say that $f$ is strongly convex over $C$ with coefficient $\sigma$ if for all $x, y \in C$ and all $\alpha \in [0,1],$ we have $$f\left(\alpha x +(1-\alpha)y\right) + \dfrac{\sigma}{2} \alpha(1-\alpha) \|x - y\|^2 \leq \alpha f(x) + (1- \alpha)f(y).$$ Show that if $f$ is strongly convex over $C$ with coefficient $\sigma$, then $f$ is strictly convex over $C$. Furthermore, there exists a unique $x^* \in C$ that minimises $f$ over $C$ and we have $$f(x) \geq f(x^*) + \dfrac{\sigma}{2} \|x - x^*\|^2.$$""",
        "answer": r"http://www.athenasc.com/convexdualitysol1.pdf"
    },
    {
        "question": r"""Let $X$ be a nonempty subset of $\mathbb{R}^n$. Show that convex hull of $X$ coincides with the set of all convex combinations of its elements. That is, $$\text{conv}(X) = \left\{ \sum_{i \in I} \alpha_i x_i ~\vert ~ I: \text{a finite set,}~ \sum_{i \in I} \alpha_i = 1, a_i \geq 0, x_i \in X, \forall i \in I\right\}.$$""",
        "answer": r"http://www.athenasc.com/convexdualitysol1.pdf"
    },
    {
        "question": r"""Show that the function $f(x) = \dfrac{1}{1-x} $ is convex for $x \in (-\infty,1]$.""",
        "answer": r"https://www.math.cmu.edu/~lohp/docs/math/mop2013/convexity-soln.pdf"
    },
    {
        "question": r"""For any constant $c \in \mathbb{R}$, show that the function $f(x) = \dfrac{x^2}{c-x} $ is convex for $x \in (-\infty,c]$.""",
        "answer": r"https://www.math.cmu.edu/~lohp/docs/math/mop2013/convexity-soln.pdf"
    },
    {
        "question": r"""Show that the function $f(x) = \dfrac{x(x-1)}{2}$ is convex.""",
        "answer": r"https://www.math.cmu.edu/~lohp/docs/math/mop2013/convexity-soln.pdf"
    },
    {
        "question": r"""Show that the function $f(x) = \dfrac{x(x-1)\cdots(x - r + 1)}{r!}$ is convex for $r \geq 1$.""",
        "answer": r"https://www.math.cmu.edu/~lohp/docs/math/mop2013/convexity-soln.pdf"
    },
    {
        "question": r"""Let $x_1, \cdots, x_n$ be positive numbers summing to $1$. By considering the function $f(x) = \dfrac{x}{\sqrt{1-x}}$, show that $$\sum_{i = 1}^n \dfrac{x_i}{\sqrt{1-x_i}} \geq \sqrt{\dfrac{n}{n-1}}.$$""",
        "answer": r"https://www.math.cmu.edu/~lohp/docs/math/mop2013/convexity-soln.pdf"
    },
    {
        "question": r"""Prove that the function $f(x_1, x_2) = \dfrac{x_1 x_2}{x_1 - x_2}$ is convex on the set $\{x \in \mathbb{R}^2: x_1 - x_2 > 0\}$.""",
        "answer": r"http://pages.di.unipi.it/passacantando/om/1-convexity.pdf"
    },
    {
        "question": r"""Prove that the function $f(x_1, x_2) = \dfrac{1}{x_1x_2}$ is convex on the set $\{x \in \mathbb{R}^2: x_1,  x_2 > 0\}$.""",
        "answer": r"http://pages.di.unipi.it/passacantando/om/1-convexity.pdf"
    },
    {
        "question": r"""Consider the convex set $C = \text{conv} \left(\{\boldsymbol{x} \in \mathbb{R}^2~:~x_1^2 + (x_2 - 1)^2 = 1\} \cup \{\boldsymbol{x} \in \mathbb{R}^2~:~x_1^2 + (x_2 + 1)^2 = 1\}  \right).$ Express $C$ in the form $\displaystyle \bigcap_{i\in I} \{x~:~f_i(x) \leq 0\},$ where $f_i: \mathbb{R}^n \mapsto \mathbb{R}.$""",
        "answer": r"http://pages.di.unipi.it/passacantando/om/1-convexity.pdf"
    },
    {
        "question": r"""Consider the convex set $C = \text{conv} \left(\{\boldsymbol{x} \in \mathbb{R}^2~:~x_1x_2 = 1\} \right).$ Express $C$ in the form $\displaystyle \bigcap_{i\in I} \{x~:~f_i(x) \leq 0\},$ where $f_i: \mathbb{R}^n \mapsto \mathbb{R}.$""",
        "answer": r"http://pages.di.unipi.it/passacantando/om/1-convexity.pdf"
    },
        {
        "question": r"""A set $C$ is midpoint convex if whenever two points $a$ and $b$ are in $C$, then the midpoint $m = \dfrac{a + b}{2}$ is also in $C$. Prove that of $C$ is closed and midpoint convex, then $C$ is convex.""",
        "answer": r"https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf"
    },
    {
        "question": r"""Let $C \subseteq \mathbb{R}^n$ be the solution set of a quadratic inequality $$C = \{\boldsymbol{x} \in \mathbb{R}^n~|~\boldsymbol{x}^TA\boldsymbol{x} + \boldsymbol{b}^T\boldsymbol{x} + c \leq 0\},$$with $A \in S^n$, $\boldsymbol{b} \in \mathbb{R}^n$ and $c \in \mathbb{R}.$
                        <ol type="i">
                        <li>Show that $C$ is convex if $A \succeq 0$.</li>
                        <li>Show that the intersection of $C$ and the hyperplane defined by $\boldsymbol{g}^T\boldsymbol{x} + h = 0$, where $\boldsymbol{g} \neq \boldsymbol{0}$, is convex if $A + \lambda \boldsymbol{g}\boldsymbol{g}^T \succeq 0$ for some $\lambda \in \mathbb{R}$.</li>
                        <li>Are the converses of these statements true? Prove your answers.</li>
                        </ol>""",
        "answer": r"https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf"
    },
        {
        "question": r"""A slab is a set of the form $\{x \in \mathbb{R}^n~|~\alpha \leq \boldsymbol{a}^T\boldsymbol{x} \leq \beta\},$ where $\alpha$ and $\beta$ are scalar values. Show that all slabs are convex and sketch a diagram of the region.""",
        "answer": r"https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf"
    },
    {
        "question": r"""A rectangle is a set of the form $\{x \in \mathbb{R}^n~|~\alpha_i \leq x_i \leq \beta_i, i = 1, \cdots, n\},$ where all $\alpha_i$ and $\beta_i$ are scalar values. Show that all rectangles are convex and sketch a diagram of the region.""",
        "answer": r"https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf"
    },
        {
        "question": r"""A wedge is a set of the form $\{x \in \mathbb{R}^n~|~\boldsymbol{a}_1^T\boldsymbol{x} \leq b_1, \boldsymbol{a}_2^T\boldsymbol{x} \leq b_2\},$ where $\boldsymbol{a}_1, \boldsymbol{a}_2 \in \mathbb{R}^n$ and $b_1, b_2 \in \mathbb{R}$ and are distinct. Show that all wedges are convex and sketch a diagram of the region.""",
        "answer": r"https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf"
    },
    {
        "question": r"""Show that the set of points closer to a given point than a given set is convex. That is, show that the set $$\{x~|~ \|\boldsymbol{x} - \boldsymbol{x}_0\|_2 \leq \|\boldsymbol{x} - \boldsymbol{y}\|_2, \forall \boldsymbol{y} \in S\},$$ where $S \subseteq \mathbb{R}^n,$ is convex.""",
        "answer": r"https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf"
    },
        {
        "question": r"""Consider the set $C = \{\boldsymbol{x} ~|~ \boldsymbol{x} + S_2 \subseteq S_1\},$ where $S_1, S_2 \subseteq \mathbb{R}^n$ with $S_1$ convex. Show that $C$ is convex.""",
        "answer": r"https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf"
    },
    {
        "question": r"""Consider the function $f: \mathbb{R}^n \mapsto \mathbb{R}$ such that $f(\boldsymbol{x}) = \|A\boldsymbol{x} - \boldsymbol{b}\|$, where $A \in \mathbb{R}^{m \times n}$, $b \in \mathbb{R}^m$ and $\| \cdot\|$ is a norm on $\mathbb{R}^m$. Show that $f$ is convex.""",
        "answer": r"https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf"
    },
        {
        "question": r"""Consider the function $f: \mathbb{R}^n \mapsto \mathbb{R}$ such that $f(\boldsymbol{x}) = \max_{i = 1, \cdots, k}\|A^{(i)}\boldsymbol{x} - \boldsymbol{b}^{(i)}\|$, where $A^{(i)} \in \mathbb{R}^{m \times n}$, $b^{(i)} \in \mathbb{R}^m$ and $\| \cdot\|$ is a norm on $\mathbb{R}^m$. Show that $f$ is convex.""",
        "answer": r"https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf"
    },
]

def generate():
    return random.choice(questions)

