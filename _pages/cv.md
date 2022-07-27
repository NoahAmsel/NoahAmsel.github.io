---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Courant Institute, New York University &emsp;&emsp; September 2022 - Present
Ph.D. in Computer Science
* Yale University &emsp;&emsp; August 2016 - May 2020  
B.S. in Computer Science & Mathematics, with distinction. Magna Cum Laude.  
Thesis: “Online Vector Balancing in Practice.” Advised by Dan Spieman.

Experience
======
* Qualcomm Technologies, Inc. &emsp;&emsp; November 2021 - July 2022  
Engineer, Corporate Research & Development &emsp;&emsp; New York, NY
  * Stayed on after Reservoir Labs was acquired by Qualcomm and turned into a new R&D division.

* Reservoir Labs &emsp;&emsp; June 2020 - November 2021  
Research Engineer &emsp;&emsp; New York, NY
  * Building software package for non-convex polynomial optimization via semidefinite programming.
  * Created algorithm for simulating network performance that achieved order-of-magnitude speed up.
  * Developed quantitative framework for designing provably efficient data center networks.
  * Deployed our network modeling tool to DOE’s Energy Sciences Network.

* Weizmann Institute of Science &emsp;&emsp; June - August 2019  
Kupcinet-Getz International Summer School, Fellow &emsp;&emsp; Rehovot, Israel
  * Developed novel spectral method for fitting latent tree graphical models of DNA data.
  * Proved sufficient condition for the algorithm to succeed and finite sample guarantee.
  * Wrote open source implementation that scales to to very large problems with high accuracy.

* Facebook, Inc. &emsp;&emsp; May - August 2018  
Software Engineering Intern &emsp;&emsp; New York, NY
  * Built Bandwidth Estimation model for Adaptive Bitrate Streaming to improve mobile video quality.
  * Implemented and tested the model in C++ and Java; refactored ABR code.
  * Validated new model in production; found it reduced error by more than half (RMSE).
  * Received return offer.

* Off the Hook, LLC &emsp;&emsp; May - July 2017  
Data Analyst / Software Developer &emsp;&emsp; New York, NY
  * Developed computer gambling software in Python based on statistical analysis of horse racing data.
  * Made race predictions and evaluated wager opportunities by using machine learning methods (Multi-
nomial Logit Model, GAM, Random Forest, PCA) and the Python scientific stack.
  * Analyzed SQL database with 3 million entries and interfaced with RESTful API.
  * Ample responsibility and independence; employer had no programming or machine learning background.

* Yale Brain Function Laboratory &emsp;&emsp; Summer 2014, 2015  
Research Assistant &emsp;&emsp; New Haven, CT
  * Wrote MATLAB programs to analyze functional Near Infrared Spectroscopy data at the gigabyte scale.
  * Introduced permutation testing for statistical significance; learned signal processing methods.
  * Designed and conducted independent, award-winning research project that used human subjects to study the neural circuitry of interpersonal communication (Intel STS Semifinalist, 2016)

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Awards
======
* Phi Beta Kappa, 2020
* Intel Science Talent Search Semifinalist, 2016

Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
