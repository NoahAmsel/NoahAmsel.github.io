---
title: "Spectral Neighbor Joining for Reconstruction of Latent Tree Models"
collection: "publications"
permalink: "/publication/2021-spectral-neighbor-joining-for-reconstruction"
date: "2021-01-01"
publication_authors: "Ariel Jaffe, Noah Amsel, Yariv Aizenbud, Boaz Nadler, Joseph T. Chang, and Yuval Kluger"
venue: "SIAM Journal on Mathematics of Data Science (SIMODS)"
paperurl: "https://doi.org/10.1137/20M1365715"
pdf_url: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8194222/pdf/nihms-1702804.pdf"
code_url: "https://github.com/NoahAmsel/spectral-tree-inference"
---
A common assumption in multiple scientific applications is that the distribution of observed data can be modeled by a latent tree graphical model. An important example is phylogenetics, where the tree models the evolutionary lineages of a set of observed organisms. Given a set of independent realizations of the random variables at the leaves of the tree, a key challenge is to infer the underlying tree topology. In this work we develop spectral neighbor joining (SNJ), a novel method to recover the structure of latent tree graphical models. Given a matrix that contains a measure of similarity between all pairs of observed variables, SNJ computes a spectral measure of cohesion between groups of observed variables. We prove that SNJ is consistent and derive a sufficient condition for correct tree recovery from an estimated similarity matrix. Combining this condition with a concentration of measure result on the similarity matrix, we bound the number of samples required to recover the tree with high probability. We illustrate via extensive simulations that in comparison to several other reconstruction methods, SNJ requires fewer samples to accurately recover trees with a large number of leaves or long edges.
