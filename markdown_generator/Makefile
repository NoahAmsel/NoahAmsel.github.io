all: ../_publications ../_talks

../_publications: generate_publications.py ../cv/publications.bib
	python generate_publications.py ../cv/publications.bib ../_publications

../_talks: talks.py talks.tsv
	python talks.py
