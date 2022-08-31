all: ../_publications ../_talks

../_publications: generate_publications.py utils.py ../cv/publications.bib
	python generate_publications.py ../cv/publications.bib ../_publications
	touch ../_publications

../_talks: generate_talks.py utils.py talks.json
	python generate_talks.py talks.json ../_talks
	touch ../_talks
