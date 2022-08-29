cv.pdf: cv.tex publications.bib resume.cls
	latexmk -pdf

publications: generate_publications.py publications.bib
	python generate_publications.py publications.bib ../_publications

clean:
	latexmk -pdf -c