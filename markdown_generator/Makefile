talks.py: talks.ipynb
	jupyter nbconvert --to script 'talks.ipynb'

talks: talks.py talks.tsv
	ipython talks.py
