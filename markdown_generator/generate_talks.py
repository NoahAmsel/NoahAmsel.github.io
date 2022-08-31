import datetime
import json
import os.path
import sys

from inspect import cleandoc

from utils import *

with open(sys.argv[1]) as f:
    talks_data = json.load(f)

for talks_data in talks_data:
    date = datetime.datetime.strptime(talks_data["date"], "%Y-%m-%d").date()
    url_slug = '-'.join((date.isoformat(), *urlify(talks_data["title"]).split('-')[:5]))
    extras = {name: talks_data[name] for name in ('pdf_url', 'video_url', 'slides_url', 'code_url') if name in talks_data}

    with open(os.path.join(sys.argv[2], f"{url_slug}.md"), 'w') as f:
        f.write(markdown_page(
            talks_data["description"],
            title=talks_data["title"],
            collection="talks",
            type=talks_data["type"],
            permalink=f"/talks/{url_slug}",
            venue=talks_data["venue"],
            date=date.isoformat(),
            location=talks_data["location"],
            published=talks_data["published"],
            **extras
        ))
