''' NYT query urls '''
#https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=section_name:%22Opinion%22%20AND%20news_desk:%22Editorial%22&sort=newest&begin_date=20190615&end_date=20190615&api-key=<your key>

#https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=pub_date:(%222019-06-15%22)%20AND%20type_of_material:(%22Editorial%22)&sort=newest&api-key=<your key>
from datetime import datetime
import requests
import spacy
import webbrowser
import os
from highlight import mark_if_needed

nlp = spacy.load('en_core_web_sm')


url = f'''https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=pub_date:("{datetime.today().year}-{datetime.today().month}-{datetime.today().day-1}") AND type_of_material:("Editorial")&sort=newest&api-key=<your key>'''
print(url)
r = requests.get(url)
editorials = r.json()['response']['docs']
print(f'{len(editorials)} editorials found')

headlines = []
for editorial in editorials:
    headlines.append(editorial['headline']['main'])

snippets = []
for editorial in editorials:
    snippets.append(editorial['snippet'])

web_url = []
for editorial in editorials:
    web_url.append(editorial['web_url'])

image_url = []
for editorial in editorials:
    image_url.append(editorial['multimedia'][0]['url'])

r = []
for url in web_url:
    r.append(requests.get(url))

i_r = []
for url in image_url:
    i_r.append(requests.get(f'https://static01.nyt.com/{url}'))


from bs4 import BeautifulSoup

for _, i_u, h, s in zip(r, image_url, headlines, snippets):
    soup = BeautifulSoup(_.content, "lxml")

#def find_correct_section(tag):
#    if tag.has_attr('name'):
#        if tag['name'] == 'articleBody':
#            return True
#    else:
#        return False
    dst_soup = BeautifulSoup('', 'html.parser')
    i = BeautifulSoup()
    #####
    head = i.new_tag('h1')
    head.string = h
    dst_soup.append(head)
    #####
    im = i.new_tag('img', src=f'https://static01.nyt.com/{i_u}')
    dst_soup.append(im)
    #####
    snip = i.new_tag('h6')
    snip.string = s
    dst_soup.append(snip)
    #####

    for sec in soup.find_all('section', attrs={'name':'articleBody'}):
        for p in sec.find_all('p')[:-2]:
            print(p.text)
            s = BeautifulSoup()
            pp = BeautifulSoup()
            par = pp.new_tag('p')
            for sent in mark_if_needed(p.text):
                if sent[0] is 1:
                    m = s.new_tag('mark')
                    m.append(sent[1])
                    par.append(m)
                else:
                    par.append(sent[1])
            dst_soup.append(par)
            #with open('nyt.html', 'a+') as f:
            #    f.write(p.text)
    print("**************************************************************")
    print("**************************************************************")
    html = dst_soup.prettify("utf-8")
    with open("template.html", "ab") as file:
        file.write(html)

filename = 'file:///'+os.getcwd()+'/' + 'template.html'
webbrowser.open_new_tab(filename)

#https://static01.nyt.com/
