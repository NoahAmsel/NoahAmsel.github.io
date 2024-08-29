---
title: "On the Benefits of Rank in Attention Layers"
collection: "publications"
permalink: "/publication/2024-on-the-benefits-of-rank"
date: "2024-01-01"
publication_authors: "Noah Amsel, Gilad Yehudai, and Joan Bruna"
venue: "arXiv Preprint"
paperurl: "https://arxiv.org/abs/2407.16153"
---
Attention-based mechanisms are widely used in machine learning, most prominently in transformers. However, hyperparameters such as the rank of the attention matrices and the number of heads are scaled nearly the same way in all realizations of this architecture, without theoretical justification. In this work we show that there are dramatic trade-offs between the rank and number of heads of the attention mechanism. Specifically, we present a simple and natural target function that can be represented using a single full-rank attention head for any context length, but that cannot be approximated by low-rank attention unless the number of heads is exponential in the embedding dimension, even for short context lengths. Moreover, we prove that, for short context lengths, adding depth allows the target to be approximated by low-rank attention. For long contexts, we conjecture that full-rank attention is necessary. Finally, we present experiments with off-the-shelf transformers that validate our theoretical findings.
