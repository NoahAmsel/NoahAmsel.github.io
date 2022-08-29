---
title: "Computing Bottleneck Structures at Scale for High-Precision Network Performance Analysis"
collection: "publications"
permalink: "/publication/2020-computing-bottleneck-structures-at-scale"
date: "2020-11-01"
publication_authors: "Noah Amsel, Jordi Ros-Giralt, Sruthi Yellamraju, James Ezick, Brendan von Hofe, Alison Ryan, and Richard Lethin"
venue: "2020 IEEE/ACM Innovating the Network for Data-Intensive Science (INDIS)"
paperurl: "https://ieeexplore.ieee.org/document/9307175"
pdf_url: "https://www.osti.gov/servlets/purl/1839037"
slides_url: "https://scinet.supercomputing.org/community/documents/110/INDIS20_PaperTalk_BottleneckStructures.pdf"
---
The Theory of Bottleneck Structures is a recently-developed framework for studying the performance of data networks. It describes how local perturbations in one part of the network propagate and interact with others. This framework is a powerful analytical tool that allows network operators to make accurate predictions about network behavior and thereby optimize performance. Previous work implemented a software package for bottleneck structure analysis, but applied it only to toy examples. In this work, we introduce the first software package capable of scaling bottleneck structure analysis to production-size networks. Here, we benchmark our system using logs from ESnet, the Department of Energy's high-performance data network that connects research institutions in the U.S. Using the previously published tool as a baseline, we demonstrate that our system achieves vastly improved performance, constructing the bottleneck structure graphs in 0.21 s and calculating link derivatives in 0.09 s on average. We also study the asymptotic complexity of our core algorithms, demonstrating good scaling properties and strong agreement with theoretical bounds. These results indicate that our new software package can maintain its fast performance when applied to even larger networks. They also show that our software is efficient enough to analyze rapidly changing networks in real time. Overall, we demonstrate the feasibility of applying bottleneck structure analysis to solve practical problems in large, real-world data networks.
