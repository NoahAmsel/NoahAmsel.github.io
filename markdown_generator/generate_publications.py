import datetime
import os.path
import sys

from inspect import cleandoc
from pybtex.database import parse_file

from utils import *

type2venue_tag = {
    'article': 'journal',
    'inproceedings': 'booktitle',
    'misc': 'publisher'
}

# This is the order their tags will appear
extras_tags = ['pdf_url', 'video_url', 'slides_url', 'poster_url', 'code_url']


def person2string(person):
    return " ".join(person.first_names + person.middle_names + person.prelast_names + person.last_names + person.lineage_names)


bib_data = parse_file(sys.argv[1])

for bib_id, bib_entry in bib_data.entries.items():
    fields = bib_entry.fields
    date = datetime.date(year=int(fields['year']), month=month2int(fields.get('month', '1')), day=int(fields.get('day', 1)))
    url_slug = '-'.join((str(date.year), *urlify(fields['title']).split('-')[:5]))
    venue_tag = type2venue_tag.get(bib_entry.type, None)
    venue = fields[venue_tag] if venue_tag else None
    authors = oxford_comma([person2string(author) for author in bib_entry.persons['author']])
    extras = {name: fields[name] for name in extras_tags if name in fields}

    with open(os.path.join(sys.argv[2], f"{url_slug}.md"), 'w') as f:
        f.write(markdown_page(
            fields['abstract'],
            title=fields['title'],
            collection="publications",
            permalink=f"/publication/{url_slug}",
            date=date.isoformat(),
            publication_authors=authors,
            venue=venue,
            paperurl=fields['url'],
            **extras
        ))
