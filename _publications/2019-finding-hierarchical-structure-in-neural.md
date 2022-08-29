---
title: "Finding Hierarchical Structure in Neural Stacks Using Unsupervised Parsing"
collection: publications
permalink: /publication/2019-finding-hierarchical-structure-in-neural
date: 2019-08-01
publication_authors: "William Merrill, Lenny Khazan, Noah Amsel, Yiding Hao, Simon Mendelsohn, and Robert Frank"
venue: "Proceedings of the 2019 ACL Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP"
paperurl: "https://aclanthology.org/W19-4823"
pdf_url: "https://aclanthology.org/W19-4823.pdf"
code_url: "https://github.com/viking-sudo-rm/industrial-stacknns"
---
Neural network architectures have been augmented with differentiable stacks in order to introduce a bias toward learning hierarchy-sensitive regularities. It has, however, proven difficult to assess the degree to which such a bias is effective, as the operation of the differentiable stack is not always interpretable. In this paper, we attempt to detect the presence of latent representations of hierarchical structure through an exploration of the unsupervised learning of constituency structure. Using a technique due to Shen et al. (2018a,b), we extract syntactic trees from the pushing behavior of stack RNNs trained on language modeling and classification objectives. We find that our models produce parses that reflect natural language syntactic constituencies, demonstrating that stack RNNs do indeed infer linguistically relevant hierarchical structure.