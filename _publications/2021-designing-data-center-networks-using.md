---
title: "Designing Data Center Networks Using Bottleneck Structures"
collection: publications
permalink: /publication/2021-designing-data-center-networks-using
date: 2021-01-01
publication_authors: "Jordi Ros-Giralt, Noah Amsel, Sruthi Yellamraju, James Ezick, Richard Lethin, Yuang Jiang, Aosong Feng, Leandros Tassiulas, Zhenguo Wu, Min Yee Teh, and Keren Bergman"
venue: "Proceedings of the 2021 ACM SIGCOMM 2021 Conference"
paperurl: "https://doi.org/10.1145/3452296.3472898"
pdf_url: "https://dl.acm.org/doi/pdf/10.1145/3452296.3472898"
video_url: "https://www.youtube.com/watch?v=s531GDw5pxs&t=2m10s&list=PLU4C2_kotFP2RrGAKLkVNGrrS8o6G-jvi&index=10"
---
This paper provides a mathematical model of data center performance based on the recently introduced Quantitative Theory of Bottleneck Structures (QTBS). Using the model, we prove that if the traffic pattern is textit{interference-free}, there exists a unique optimal design that both minimizes maximum flow completion time and yields maximal system-wide throughput. We show that interference-free patterns correspond to the important set of patterns that display data locality properties and use these theoretical insights to study three widely used interconnects---fat-trees, folded-Clos and dragonfly topologies. We derive equations that describe the optimal design for each interconnect as a function of the traffic pattern. Our model predicts, for example, that a 3-level folded-Clos interconnect with radix 24 that routes 10% of the traffic through the spine links can reduce the number of switches and cabling at the core layer by 25% without any performance penalty. We present experiments using production TCP/IP code to empirically validate the results and provide tables for network designers to identify optimal designs as a function of the size of the interconnect and traffic pattern.