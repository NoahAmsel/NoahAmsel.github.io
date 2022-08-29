import datetime
import os.path
import re
import sys

from inspect import cleandoc
from pybtex.database import parse_file

bib_data = parse_file(sys.argv[1])

def pub_page(title, url_slug, date, venue, external_url, authors, abstract, **kwargs):
    extra_args = "\n    ".join(f'{name}: "{value}"' for name, value in kwargs.items())

    return cleandoc(f"""---
    title: "{title}"
    collection: publications
    permalink: /publication/{url_slug}
    date: {date.isoformat()}
    publication_authors: "{authors}"
    venue: "{venue}"
    paperurl: "{external_url}"
    {extra_args}
    ---
    {abstract}

    """)


def html_escape(text):
    """Produce entities within text."""
    html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&apos;"
    }
    return "".join(html_escape_table.get(c,c) for c in text)

def month2int(month_str):
    month2num = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7, 
        "august": 8, 
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12
    }
    if month_str.isdigit():
        return int(month_str)
    else:
        return month2num[month_str.lower()]

def urlify(s):
    # https://stackoverflow.com/questions/1007481/how-to-replace-whitespaces-with-underscore
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)
    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)
    return s.lower()

type2venue_tag = {
    'article': 'journal',
    'inproceedings': 'booktitle'
}

def person2string(person):
    return " ".join(person.first_names + person.middle_names + person.prelast_names + person.last_names + person.lineage_names)

def oxford_comma(l):
    if len(l) <= 2:
        return " and ".join(l)
    else:
        return ", ".join(l[:-1]) + ", and " + l[-1]

for bib_id, bib_entry in bib_data.entries.items():
    fields = bib_entry.fields
    date = datetime.date(year=int(fields['year']), month=month2int(fields.get('month', '1')), day=int(fields.get('day', 1)))
    url_slug = '-'.join((str(date.year), *urlify(fields['title']).split('-')[:5]))
    venue_tag = type2venue_tag.get(bib_entry.type, None)
    venue = fields[venue_tag] if venue_tag else None
    authors = oxford_comma([person2string(author) for author in bib_entry.persons['author']])
    extras = {name: fields[name] for name in ('pdf_url', 'video_url', 'slides_url', 'code_url') if name in fields}

    with open(os.path.join(sys.argv[2], f"{url_slug}.md"), 'w') as f:
        f.write(pub_page(fields['title'], url_slug, date, venue, fields['url'], authors, fields['abstract'], **extras))
