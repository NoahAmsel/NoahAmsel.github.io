all: ../_publications ../_talks

../_publications: generate_publications.py utils.py ../cv/publications.bib
	python generate_publications.py ../cv/publications.bib ../_publications

../_talks: generate_talks.py utils.py talks.tsv
	python generate_talks.py talks.tsv ../_talks