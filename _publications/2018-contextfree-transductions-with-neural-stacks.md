---
title: "Context-Free Transductions with Neural Stacks"
collection: publications
permalink: /publication/2018-contextfree-transductions-with-neural-stacks
date: 2018-11-01
publication_authors: "Yiding Hao, William Merrill, Dana Angluin, Robert Frank, Noah Amsel, Andrew Benz, and Simon Mendelsohn"
venue: "Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP"
paperurl: "https://aclanthology.org/W18-5433"
pdf_url: "https://aclanthology.org/W18-5433.pdf"
code_url: "https://github.com/viking-sudo-rm/StackNN"
---
This paper analyzes the behavior of stack-augmented recurrent neural network (RNN) models. Due to the architectural similarity between stack RNNs and pushdown transducers, we train stack RNN models on a number of tasks, including string reversal, context-free language modelling, and cumulative XOR evaluation. Examining the behavior of our networks, we show that stack-augmented RNNs can discover intuitive stack-based strategies for solving our tasks. However, stack RNNs are more difficult to train than classical architectures such as LSTMs. Rather than employ stack-based strategies, more complex networks often find approximate solutions by using the stack as unstructured memory.