talks.py: talks.ipynb
	jupyter nbconvert --to script 'talks.ipynb'

talks: talks.py talks.tsv
	ipython talks.py

pubs.bib:
	curl "https://scholar.googleusercontent.com/citations?view_op=export_citations&user=vkykpWgAAAAJ&citsig=AMD79ooAAAAAYuIeblQ2uqJnppXiPL8rsfGf2r5ox0b3&hl=en" -o pubs.bib

pubsFromBib.py: PubsFromBib.ipynb
	jupyter nbconvert --to script 'PubsFromBib.ipynb' --output pubsFromBib

publications.py: publications.ipynb
	jupyter nbconvert --to script 'publications.ipynb'

publications: publications.py publications.tsv
	ipython publications.py
