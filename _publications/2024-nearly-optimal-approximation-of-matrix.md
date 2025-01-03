---
title: "Nearly Optimal Approximation of Matrix Functions by the Lanczos Method"
collection: "publications"
permalink: "/publication/2024-nearly-optimal-approximation-of-matrix"
date: "2024-01-01"
publication_authors: "Noah Amsel, Tyler Chen, Anne Greenbaum, Cameron N Musco, and Christopher Musco"
venue: "The Thirty-eighth Annual Conference on Neural Information Processing Systems"
paperurl: "https://openreview.net/forum?id=3s8V8QP9XV"
poster_url: "/files/icerm_poster.pdf"
code_url: "https://github.com/NoahAmsel/lanczos-optimality/tree/near_optimality_paper"
---
We study the Lanczos method for approximating the action of a symmetric matrix function f(A) on a vector b (Lanczos-FA). For the function A^{-1}, it is known that the error of Lanczos-FA after k iterations matches the error of the best approximation from the Krylov subspace of degree k when A is positive definite. We prove that the same holds, up to a multiplicative approximation factor, when f is a rational function with no poles in the interval containing A's eigenvalues. The approximation factor depends the degree of f's denominator and the condition number of A, but not on the number of iterations k. Experiments confirm that our bound accurately predicts the convergence of Lanczos-FA. Moreover, we believe that our result provides strong theoretical justification for the excellent practical performance that has long by observed of the Lanczos method, both for approximating rational functions and functions like A^{1/2}b that are well approximated by rationals.
