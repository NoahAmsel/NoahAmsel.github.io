all: cv.pdf

cv.pdf: cv.tex publications.bib resume.cls
	latexmk -pdf
	latexmk -pdf -c

google_pubs.bib:
	curl "https://scholar.googleusercontent.com/citations?view_op=export_citations&user=vkykpWgAAAAJ&citsig=AMD79ooAAAAAYuIeblQ2uqJnppXiPL8rsfGf2r5ox0b3&hl=en" -o google_pubs.bib
