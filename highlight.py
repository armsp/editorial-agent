import spacy
nlp = spacy.load('en_core_web_sm')
from bs4 import BeautifulSoup

html_doc = '''<p>For a country that takes pride in the venerable stability of its democracy, Britain is strangely prone to constitutional improvisations. For example, if the current <a href="https://www.theguardian.com/politics/conservative-leadership" title="">Conservative party leadership contest</a> proceeds as far as a ballot of party members, it will be the first time a prime minister is chosen by that method.</p> <p>This year, those leaders — Gov. Andrew Cuomo; the Senate majority leader, Andrea Stewart-Cousins; and the Assembly speaker, Carl Heastie — deserve significant credit. This sentence should not be marked.</p> <p> This sentence should not be marked. This year, those leaders — Gov. Andrew Cuomo; the Senate majority leader, Andrea Stewart-Cousins; and the Assembly speaker, Carl Heastie — deserve significant credit.</p> <p>This year, those leaders — Gov. Andrew Cuomo; the Senate majority leader, Andrea Stewart-Cousins; and the Assembly speaker, Carl Heastie — deserve significant credit.</p> <p>This year, those leaders — Gov. Andrew Cuomo; the Senate majority leader, Andrea Stewart-Cousins; and the Assembly speaker, Carl Heastie — deserve significant credit. This year, those leaders — Gov. Andrew Cuomo; the Senate majority leader, Andrea Stewart-Cousins; and the Assembly speaker, Carl Heastie — deserve significant credit.</p> <p>This is an unmarked random sentence. This year, those leaders — Gov. Andrew Cuomo; the Senate majority leader, Andrea Stewart-Cousins; and the Assembly speaker, Carl Heastie — deserve significant credit. Another unmarked random sentnce.</p>'''

src_soup = BeautifulSoup(html_doc, 'html.parser') #BeautifulSoup(html_doc, 'html.parser')
dst_soup = BeautifulSoup('', 'html.parser')

#WORDS_TO_LOOK_FOR = ['Britain', 'party']
import re

semicolon_re = ";"
colon_re = ":"
dash_re = "( — )+|( - )+"


def mark_if_needed(text):
    doc = nlp(text)
    for sent in doc.sents:
        check = re.search(semicolon_re, sent.text) or re.search(colon_re, sent.text) or re.search(dash_re, sent.text) #need to check if all instances are found. Most probably yes because we deal with a single sentence at a time.
        if check is None:
            yield (0, sent.text)
        else:
            yield (1, sent.text)



p_elements = src_soup.find_all('p')
for p in p_elements:
    s = BeautifulSoup()
    pp = BeautifulSoup()
    par = pp.new_tag('p')
    #a_elements = p.find_all('a')
    #p.string = mark_if_needed(p.text)
    #new_str=''
    #p.clear()
    for sent in mark_if_needed(p.text):
        print(f'returned sentence is {sent}')
        #p.clear()
        #new_str+=sent[1]

        if sent[0] is 1:
            m = s.new_tag('mark')
            #m.string = sent[1]
            m.append(sent[1])
            #p.insert_after(m)
            par.append(m)

        else:
            par.append(sent[1])
            #if p.string:
            #    p.string+=sent[1]
            #new_str+=sent[1]

    #p.string = new_str
    dst_soup.append(par)
    #for a in a_elements:
        #a.string = mark_if_needed(a.text)
        #p.append(a)

print(dst_soup.prettify())
html = dst_soup.prettify("utf-8")
with open("output.html", "wb") as file:
    file.write(html)