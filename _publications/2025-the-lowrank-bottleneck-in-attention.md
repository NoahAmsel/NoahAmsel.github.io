---
title: "The Low-Rank Bottleneck in Attention"
collection: "publications"
permalink: "/publication/2025-the-lowrank-bottleneck-in-attention"
date: "2025-01-01"
publication_authors: "Noah Amsel, Gilad Yehudai, and Joan Bruna"
venue: "The Thirteenth International Conference on Learning Representations"
paperurl: "https://openreview.net/forum?id=y9Xp9NozPR"
slides_url: "/files/chris_lab_meeting.pdf"
poster_url: "/files/ny_academy_poster.pdf"
code_url: "https://github.com/NoahAmsel/attention-formers"
---
Attention-based mechanisms are widely used in machine learning, most prominently in transformers. However, hyperparameters such as the rank of the attention matrices and the number of heads are scaled nearly the same way in all realizations of this architecture, without theoretical justification. In this work we show that there are dramatic trade-offs between the rank and number of heads of the attention mechanism. Specifically, we present a simple and natural target function that can be represented using a single full-rank attention head for any context length, but that cannot be approximated by low-rank attention unless the number of heads is exponential in the embedding dimension, even for short context lengths. Moreover, we prove that, for short context lengths, adding depth allows the target to be approximated by low-rank attention. For long contexts, we conjecture that full-rank attention is necessary. Finally, we present experiments with off-the-shelf transformers that validate our theoretical findings.
