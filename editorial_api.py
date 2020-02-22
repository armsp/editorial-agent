import webbrowser
import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
#import spacy
from highlight import mark_if_needed

#nlp = spacy.load('en_core_web_sm')
semicolon_re = ";"
colon_re = ":"
dash_re = "( — )+|( - )+"

guardian_endpoint = '''https://content.guardianapis.com/tone/editorials'''
guardian_key = 'd7539ac9-6ce6-43af-b4ab-a373a2bb2968'
guardian_payload = {'show-fields': 'body', 'api-key': guardian_key}


# For guardain
r = requests.get(guardian_endpoint, params=guardian_payload)

print(r.url)
print(r.status_code)
#print(r.json())
json_content = r.json()
latest_editorials_list = json_content['response']['results']
print(f'{len(latest_editorials_list)} - editorials found')


with open('helloworld.html','w') as f:
    for editorial in latest_editorials_list:
        date = datetime.strptime(editorial['webPublicationDate'], '%Y-%m-%dT%H:%M:%SZ')
        if date.day == datetime.today().day or date.day == datetime.today().day-1:
            editorial_title = editorial['webTitle']
            editorial_body = editorial['fields']['body']
            print("******************************************************")
            print(editorial_body)
            print("******************************************************")
            #f.write(editorial_body)
            src_soup = BeautifulSoup(editorial_body, 'html.parser')
            dst_soup = BeautifulSoup('', 'html.parser')
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
                    #print(f'returned sentence is {sent}')
                    #p.clear()
                    #new_str+=sent[1]

                    if sent[0] == 1:
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


            html = dst_soup.prettify("utf-8")
            with open(f"helloworld-{str(date)}.html", "wb") as file:
                file.write(html)

            filename = 'file:///'+os.getcwd()+'/' + f'helloworld-{str(date)}.html'
            webbrowser.open_new_tab(filename)