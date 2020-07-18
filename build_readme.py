import feedparser
import pathlib
import re
import os

root = pathlib.Path(__file__).parent.resolve()

def fetch_blog_entries():
    entries = feedparser.parse("https://www.zer0-nu1l.com/atom.xml")["entries"]
    return [
        {
            "title": entry["title"],
            "url": entry["link"].split("#")[0],
            "published": entry["published"].split("T")[0],
        }
        for entry in entries
    ]


if __name__ == "__main__":
	readme = root / "README.md"
	readme_contents = readme.open().read()
    
	entries = fetch_blog_entries()[:5]
	entries_md = "\n".join(
	        ["* [{title}]({url}) - {published}".format(**entry) for entry in entries]
	    )

	with open(readme, 'w') as f:
		f.write('## Recent releases\n\n')
		f.write(entries_md)
