Config `enable_darkmode` to false, but then the dates under news and latest posts stay in white color text. note that on chrome it seems to work fine?

Move socials up to where they were with the old site. trim them down
I had a few things below my picture, including a obfuscated email

Previously, I had a button that redirected to the archival version of the paper. For preprints it said (preprint) and for others it said "journal".
This theme has separate tags for arxiv and "html" but I should change the text from "html" to something more descriptive.
Actually I think we should use the arxiv doi tag for this. It seems like the "URL" in our existing bibtex is usually the same as the listed dois.
Also note that a lot of these bibtex's had URL as a field before me. I just changed them to "html" but actually if you want to use these in a latex document that might have been a mistake. we might need both
- status: I restored all the URLs. So now, each has an HTML tag and also a URL. but change the logic of bib.liquid to just use URL (or DOI if that exists)

add months to bibtex

Don't forget to chance the color and fonts and stuff
change the style of coauthors when they have hyperlinks. don't want them to outshine me

venue tags text color. make sure it looks good in both light and dark mode, and see if we can distinguish those venues which have clickable links. (I removed that distinction)

Add links to this, MAD, and say I also work with CCM at Flatiron https://cs.nyu.edu/theory-group/.

Fix the rendering of the additional_info field in the bibliography. It should come after the date.
Maybe even make a pull request it really does seem wrong.
But also see here: https://github.com/alshedivat/al-folio/pull/2325

### note on biblio buttons
in addition to those listed in CUSTOMIZE.md, the other bibtex tags used in _layouts/bib.liquid:
- preview
- additional_info
- award (this is the text that you see if you click the award button)
- award_name (this is in the buttom)
- doi
- video
- google_scholar_id
- inspirehep_id
- eprint
- pmid
- isbn