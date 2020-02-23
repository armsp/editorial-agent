import re

import spacy
from bs4 import BeautifulSoup

nlp = spacy.load('en_core_web_sm')

semicolon_re = ";"
colon_re = ":"
dash_re = "( — )+|( - )+"

def highlight(p_elements):
    paragraphs = BeautifulSoup('', 'html.parser')
    for p in p_elements:
        paragraph = BeautifulSoup('', 'html.parser').new_tag('p')
        #paragraph = paragraph_soup.new_tag('p')
        doc = nlp(p.text)
        for sent in doc.sents:
            check = re.search(semicolon_re, sent.text) or re.search(colon_re, sent.text) or re.search(dash_re, sent.text) #need to check if all instances are found. Most probably yes because we deal with a single sentence at a time.
            if check:
                mark = BeautifulSoup('', 'html.parser').new_tag('mark')
                mark.append(sent.text)
                paragraph.append(mark)
            else:
                paragraph.append(sent.text)
        paragraphs.append(paragraph)
    return paragraphs


