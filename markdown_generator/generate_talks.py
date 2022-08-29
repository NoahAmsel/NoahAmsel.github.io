import datetime
import os.path
import sys

from inspect import cleandoc
from pandas import read_csv

from utils import *

talks_table = read_csv(sys.argv[1], sep="\t", header=0, quotechar='`')

for row, item in talks_table.iterrows():
    date = datetime.datetime.strptime(item.date, "%Y-%m-%d").date()
    url_slug = '-'.join((date.isoformat(), *urlify(item.title).split('-')[:5]))
    extras = {name: item[name] for name in ('pdf_url', 'video_url', 'slides_url', 'code_url') if name in item}

    with open(os.path.join(sys.argv[2], f"{url_slug}.md"), 'w') as f:
        f.write(markdown_page(
            item.description,
            title=item.title,
            collection="talks",
            type=item.type,
            permalink=f"/talks/{url_slug}",
            venue=item.venue,
            date=date.isoformat(),
            location=item.location,
            published=item.published,
            **extras
        ))