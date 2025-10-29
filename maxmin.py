import random

questions = [
    {
        'question': r"""Find the stationary point of the function $$f(x_1, x_2, x_3) = 100 - 2x_1^2-x_2^2 - 3x_3-x_1x_2 + e^{x_1 + x_2 + x_3}$$and show that this point is a global maximum.""",
        'answer': r"http://www.mysmu.edu/faculty/anthonytay/MFE/MFE_1_Section_21.pdf",
    },
    {
        'question': r"""Show that the function $$f(x_1, x_2) = (1 + x_2)^3 x_1^2 + x_2^2$$has a local minimum at $(x_1, x_2) = (0,0)$, but that it has no global minimum.""",
        'answer': r"http://www.mysmu.edu/faculty/anthonytay/MFE/MFE_1_Section_21.pdf",
    },
    {
        'question': r"""A farmer has the production function $Y = \sqrt{N}$ for $N > 0,$ where $N$ is the amount of fertiliser put into the production process, and $Y$ is the farmer's output. Fertiliser costs $\$1$ per kilogram, and each unit of output fetches a price of $p$ dollars. Given $p$, the farmer chooses $N$ to maximise profit $$\pi(N,p) = p\sqrt{N}-N.$$
                        <ol type="i">
                        <li>Find the profit maximising level of $N$, $N^*(p)$. Find the value function $\pi^*(p) = \pi\left(N^*(p), p\right)$.</li>
                        <li>Find $\dfrac{d \pi^*(p)}{dp}.$</li>
                        <li>Find $\dfrac{\partial \pi(N, p)}{\partial p}$. Evaluate this derivative at $N = N^*(p).$ Compare this derivative with the result from the previous part.</li>
                        </ol>""",
        'answer': r"http://www.mysmu.edu/faculty/anthonytay/MFE/MFE_1_Section_21.pdf",
    },
    {
        'question': r"""Let $f(x,y)$ be such that $f_x' > 0$, $f_y' > 0$, $f_{xx}'' < 0$, $f_{yy}'' < 0$, and $f_{xx}''f_{yy}''-f_{xy}''^2 > 0$. Consider the problem $$\max \pi(x,y) = pf(x,y) - q_1 x - q_2 y$$ where $p$, $q_1$, $q_2$ are all positive. Let $x^*(p, q_1, q_2)$ and $y^*(p, q_1, q_2)$ be stationary points of the function $\pi(x, y)$.
                        <ol type="i">
                        <li>Explain why the stationary points of the function solve the maximisation problem.</li>
                        <li>Find $\dfrac{\partial x^*}{\partial q_1}$ and $\dfrac{\partial y^*}{\partial q_1}$. Show that given our assumptions, that the former is negative, but the sign of the latter cannot be determined.</li>
                        <li>A function $g(x,y)$ is homogeneous of degree $k$ if $g(tx, ty) = t^kg(x,y)$ for any $t>0$. Show that if $g(x,y)$ is homogenous of degree $k$, then $$xg_1'(x,y) + yg_2'(x,y) = kg(x,y).$$</li>
                        <li>Show that both $x^*(p, q_1, q_2)$ and $y^*(p, q_1, q_2)$ are homogenous of degree zero. That is, for any $t>0$, show that $$x^*(tp, tq_1, tq_2) = x^*(p, q_1, q_2)~~\text{and}~~y^*(tp, tq_1, tq_2) = y^*(p, q_1, q_2).$$</li>
                        <li>Is the value function $\pi^*(p, q_1, q_2)$ also homogenous? If so, to what degree?</li>
                        <li>Find $\dfrac{\partial \pi^*}{\partial p}$, $\dfrac{\partial \pi^*}{\partial q_1}$ and $\dfrac{\partial \pi^*}{\partial q_2}$. Use the latter two expressions to show that $\dfrac{\partial x^*}{\partial q_2} = \dfrac{\partial y^*}{\partial q_1}$.</li>
                        </ol>""",
        'answer': r"http://www.mysmu.edu/faculty/anthonytay/MFE/MFE_1_Section_21.pdf",
    },
    {
        'question': r"""Find and classify all the stationary points of the function $$f(x, y) = (x^2 - axy)e^y.$$Let $(x^*, y^*)$ be a stationary point of $f(x, y)$ and let $f^*(a) = f(x^*, y^*).$ Find $\dfrac{d f^*(a)}{da}$ by differentiating $f(x^*, y^*)$ directly.""",
        'answer': r"http://www.mysmu.edu/faculty/anthonytay/MFE/MFE_1_Section_21.pdf",
    },
    {
        'question': r"""Find and classify the critical points for the function $$f(x, y) = x^3 - 3xy^2 - 9x^2-6y^2 + 27.$$""",
        'answer': r"https://people.math.umass.edu/~havens/Partials.pdf",
    },
    {
        'question': r"""Find and classify the critical points for the function $$f(x, y) = \dfrac{x}{1+y^2} + \dfrac{y}{1+x^2}.$$""",
        'answer': r"https://people.math.umass.edu/~havens/Partials.pdf",
    },
    {
        'question': r"""Suppose you want to make an (open) cone out of paper. If you want the cone to have a volume of $\dfrac{4\pi}{3},$ then what would be the optimum radius and height to minimise the surface area of the cone? Recall that the area of an open cone with radius $r$ and height $h$ is $\mathcal{A}(r, h) = \pi r \sqrt{r^2 + y^2}.$""",
        'answer': r"https://people.math.umass.edu/~havens/Partials.pdf",
    },
    {
        'question': r"""Find the minimum value of $f(x, y, z) = x^2 + 4y^2 + 9z^2$ on the intersection of the hyperboloids $4x^2 + y^2 - 9z^2 = 1$ and $9x^2 - 4y^2 - z^2 = 1$. Explain why there is no maximum value of $f$ along this intersection locus.""",
        'answer': r"https://people.math.umass.edu/~havens/Partials.pdf",
    },
    {
        'question': r"""What is the shortest distance from the surface $xy + 3x + z^2 = 9$ to the origin?""",
        'answer': r"https://sites.oxy.edu/ron/math/212/15/ws/ws16.pdf",
    },
    {
        'question': r"""Find the maximum and minimum values of $f(x,y) = (x-1)^2 + (y-2)^2$ subject to the constraint $x^2 + y^2 \leq 45$.""",
        'answer': r"https://sites.oxy.edu/ron/math/212/15/ws/ws17.pdf",
    },
    {
        'question': r"""Consider the function $S(x,y) = 3xe^y - x^3 - e^{3y}.$
                    <ol type="i">
                    <li>Compute $\nabla S$.</li>
                    <li>Use your answer from the previous part to show that there is only one critical point of $S(x,y)$, at the point $(1,0,1)$.</li>
                    <li>By using $D = f_{xx}(a,b)f_{yy}(a,b) - f_{xy}^2(a,b)$, show that the point from the previous part is a local maximiser of $S(x,y)$.</li>
                    <li>Is the local maximiser from the previous part also a global maximiser of $S(x,y)$? Support your answer with calculations.</li>
                    <ol>""",
        'answer': r"https://sites.oxy.edu/ron/math/212/15/quiz/QUIZ07.pdf",
    },
    {
        'question': r"""A container with an open top is to have $10 \text{m}^3$ capacity and be made of thin sheet metal. Calculate the dimensions of the box if it is to use the minimum possible amount of material.""",
        'answer': r"http://personal.maths.surrey.ac.uk/st/S.Zelik/teach/calculus/max_min_2var.pdf",
    },
    {
        'question': r"""A construction company is tasked with creating guttering from a strip of metal 12 cm wide. To do this, let $x$ be the length of each of the sections that will form the slope, and let $\theta$ be the angle that each sloping side makes with the horizontal. Determine the values of $x$ and $\theta$ that maximise the capacity of the guttering.""",
        'answer': r"http://personal.maths.surrey.ac.uk/st/S.Zelik/teach/calculus/max_min_2var.pdf",
    },
    {
        'question': r"""A person is sailing across a circular lake with diameter $4$ kilometres. He starts at point $X$ and needs to get to point $Y$ which is diametrically opposite to $X$. To get there as quickly as possible, he will sail directly from $X$ to a point $Z$ on the shore and then walk from $Z$ to $Y$ along the rim of the lake. If he can sail at a speed of $2$ kilometres per hour and can walk $4$ kilometres per hour, what is the minimum number of hours he needs to make his trip?""",
        'answer': r"https://math.stackexchange.com/questions/2875437/calculus-optimization-problem-part-2/2875559#2875559",
    },
    {
        'question': r"""Consider the function $f(x,y) = x^2 + y^2 + \beta xy + 2x + y.$ For a given value of $y$, we can minimise with respect to $x$ by setting the derivative with respect to $x$ equal to $0$ and solving for a new value of $x$, which gives $x_\text{new} = -1 - \dfrac{\beta}{2}y$. Similarly, we can repeat the process with $y$ to yield $y_\text{new} = -\dfrac{1}{2} - \dfrac{\beta}{2} x$. Let $(x_0, y_0)$ be an initial guess for a minimiser of $f$. We compute the next estimation using the following formula: \begin{align*}x_{k+1} &= -1 -\dfrac{\beta}{2}y_k\\y_{k+1}&= -\dfrac{1}{2} - \dfrac{\beta}{2} x_k.\end{align*} For $-2 < \beta < 2$, show that $(x_k, y_k)$ converges to $(x^*, y^*)$ and that $f(x_k, y_k)$ decreases to $f(x^*, y^*)$ as $k \to \infty$. What happens outside of this range?""",
        'answer': r"https://people.cs.rutgers.edu/~cwcowan/CS674/OptimizationNotes.pdf",
    },
    {
        'question': r"""Characterise the minima of the function $f(x,y) = (x^2 + y^2 - r^2)^2$ by taking $r$ to be a constant. In general, what can be said about the minima (and maxima) of $f_p(x,y) = |x^2 + y^2 - r^2|^p$?""",
        'answer': r"https://people.cs.rutgers.edu/~cwcowan/CS674/OptimizationNotes.pdf",
    },
    {
        'question': r"""Consider the function given by $A(x, y) = x + y - 2y^2$ for $0 \leq x < y \leq 3\}$. Find the global maximum and minimum values of $A(x, y)$ without the use of calculus.""",
        'answer': r"$x \in \left[-15, \dfrac{1}{2} \right)$.",
    },
]

def generate():
    return random.choice(questions)