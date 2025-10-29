# **MATH3161 Exam Generator**

**Type:** Scripted TeX Generator · **Tech:** Python, NumPy, LaTeX · **Status:** Completed

## **Overview:**
Small generator for mathematical optimisation exam-style questions; emits a `.tex` paper you render yourself; expect occasional warnings due to some randomised question templates.

## Modules Assessed

* `conjugate_grad_method.py`: Quadratic minimisation with **conjugate gradient (Fletcher–Reeves)** prompts and proof checks. 
* `newtons_method.py`: Strictly convex quadratic tasks with **Newton direction** verification and convergence runs. 
* `steepest_descent.py`: SPD checks, steepest-descent solver and a deterministic ratio helper for iteration analysis. 
* `equality_constraints.py`: KKT **regularity / FONC / SOSC** questions for 2–3 variables with linear or circular constraints. 
* `kuhn_tucker.py`: Region sketching + convexity check + **Kuhn–Tucker** conditions with a given candidate (x^*). 
* `wolfe_dual.py`: Forms the **Wolfe dual** where applicable; otherwise asks to prove non-convexity. 
* `definiteness.py`: Random matrix; classify as PD/ND/PSD/NSD/indefinite via eigenvalues. 
* `matrix_proof.py`: Assorted linear-algebra proof prompts (idempotent, nilpotent, symmetry, PD facts). 
* `stationary.py`: Stationary-point problems (econ-flavoured maxima/minima and envelopes). 
* `maxmin.py`: General multivariate polynomial generator; **find and classify all stationary points**. 
* `concavity.py`: Hand-picked convexity/concavity questions with external solution links (listed in your message).

## Notes

* Output is LaTeX; render locally; rerun until no warnings if randomness breaks a case, especially some induction templates.
* Code is a proof-of-concept, not fully polished; correctness is not guaranteed across all seeds (your stated caveat).


