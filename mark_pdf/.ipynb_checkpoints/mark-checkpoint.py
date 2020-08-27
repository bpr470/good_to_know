#searching pdf with pymupdf
import sys
import fitz

def mark_word(page, text):
    rl = page.searchFor(text, quads=True)            
    for ix, k in enumerate(rl):
        annot = page.addHighlightAnnot(k)
        annot.setInfo({'content': f'Content-/-{ix}', 'name': '', 'title': '', 
                       'creationDate': '', 'modDate': '', 'subject': ''})

fname = sys.argv[1]                    # filename
text = sys.argv[2]                     # search string
doc = fitz.open(fname)

new_doc = False                        # indicator if anything found at all

for page in doc:                       # scan through the pages
    found = mark_word(page, text)      # mark the page's words


doc.save("marked-" + doc.name)