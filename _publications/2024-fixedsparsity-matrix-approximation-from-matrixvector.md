---
title: "Fixed-sparsity matrix approximation from matrix-vector products"
collection: "publications"
permalink: "/publication/2024-fixedsparsity-matrix-approximation-from-matrixvector"
date: "2024-01-01"
publication_authors: "Noah Amsel, Tyler Chen, Feyza Duman Keles, Diana Halikias, Cameron Musco, and Christopher Musco"
venue: "arXiv Preprint"
paperurl: "https://arxiv.org/abs/2402.09379"
---
We study the problem of approximating a matrix A with a matrix that has a fixed sparsity pattern (e.g., diagonal, banded, etc.), when A is accessed only by matrix-vector products. We describe a simple randomized algorithm that returns an approximation with the given sparsity pattern with Frobenius-norm error at most (1+ε) times the best possible error. When each row of the desired sparsity pattern has at most s nonzero entries, this algorithm requires O(s/ε) non-adaptive matrix-vector products with A. We also prove a matching lower-bound, showing that, for any sparsity pattern with Θ(s) nonzeros per row and column, any algorithm achieving (1+ϵ) approximation requires Ω(s/ε) matrix-vector products in the worst case. We thus resolve the matrix-vector product query complexity of the problem up to constant factors, even for the well-studied case of diagonal approximation, for which no previous lower bounds were known.
