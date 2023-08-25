---
title: "{Spectral top-down recovery of latent tree models}"
collection: "publications"
permalink: "/publication/2023-spectral-topdown-recovery-of-latent"
date: "2023-08-01"
publication_authors: "Yariv Aizenbud, Ariel Jaffe, Meng Wang, Amber Hu, Noah Amsel, Boaz Nadler, Joseph T Chang, and Yuval Kluger"
venue: "Information and Inference: A Journal of the IMA"
paperurl: "https://doi.org/10.1093/imaiai/iaad032"
---
{Modeling the distribution of high-dimensional data by a latent tree graphical model is a prevalent approach in multiple scientific domains. A common task is to infer the underlying tree structure, given only observations of its terminal nodes. Many algorithms for tree recovery are computationally intensive, which limits their applicability to trees of moderate size. For large trees, a common approach, termed divide-and-conquer, is to recover the tree structure in two steps. First, separately recover the structure of multiple, possibly random subsets of the terminal nodes. Second, merge the resulting subtrees to form a full tree. Here, we develop spectral top-down recovery (STDR), a deterministic divide-and-conquer approach to infer large latent tree models. Unlike previous methods, STDR partitions the terminal nodes in a non random way, based on the Fiedler vector of a suitable Laplacian matrix related to the observed nodes. We prove that under certain conditions, this partitioning is consistent with the tree structure. This, in turn, leads to a significantly simpler merging procedure of the small subtrees. We prove that STDR is statistically consistent and bound the number of samples required to accurately recover the tree with high probability. Using simulated data from several common tree models in phylogenetics, we demonstrate that STDR has a significant advantage in terms of runtime, with improved or similar accuracy.}
