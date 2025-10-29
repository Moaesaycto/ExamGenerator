import matrix_proof
import definiteness
import concavity
import maxmin
import stationary
import equality_constraints
import kuhn_tucker
import wolfe_dual
import steepest_descent
import newtons_method
import conjugate_grad_method

if __name__ == '__main__':
    questions = [
        definiteness.generate(),
        matrix_proof.generate(),
        concavity.generate(),
        maxmin.generate(),
        stationary.generate(),
        equality_constraints.generate(),
        kuhn_tucker.generate(),
        wolfe_dual.generate(),
        steepest_descent.generate(),
        newtons_method.generate(),
        conjugate_grad_method.generate()
    ]
    
    nums = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN", "TWENTY"]

    paper = r"""
    \documentclass[11pt]{article}

    \usepackage{sectsty}
    \usepackage{graphicx}
    \usepackage{amsmath}
    \usepackage{bm}
    \usepackage{amsfonts}

    % Margins
    \topmargin=-0.45in
    \evensidemargin=0in
    \oddsidemargin=0in
    \textwidth=6.5in
    \textheight=9.0in
    \headsep=0.25in

    \title{ MATH3161 - Optimisation}
    \author{ Generatively made exam by Moae }

    \begin{document}
    \maketitle
    """

    for i in range(len(questions)):
        paper += r"""
    \Large \textbf{QUESTION """ + nums[i] + r"""}

    \vspace{5pt}

    \normalsize """ + questions[i]['question'] + r"""

    \vspace{20pt}
    """
    
    paper += r"""\end{document}"""
    
    f = open("paper.tex", "w")
    f.write(paper)
    f.close()
    
