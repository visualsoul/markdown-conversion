from markdown2 import Markdown

md = Markdown()

with open("entries/CSS.md") as entry:
    text = entry.read()
    # print(text)
    result = md.convert(text=text)
    print(result)

