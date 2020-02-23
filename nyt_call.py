#import os
import logging
from datetime import datetime

import yaml
import requests
from bs4 import BeautifulSoup

from render import render_editorial
from editorial_formatter import editorial_formatter

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')

with open('.secrets.yaml') as f:
    secrets = yaml.safe_load(f)

nyt_key = secrets['NYT-KEY']

url = f'''https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=pub_date:("{datetime.today().year}-{datetime.today().month}-{datetime.today().day-1}") AND type_of_material:("Editorial")&sort=newest&api-key={nyt_key}'''
print(url)
r = requests.get(url)
if r.status_code != requests.codes.ok:#r.status != 200:
    logging.debug("No response, Aborting...")
    exit()

response_json = r.json()

editorials_meta = response_json['response']['docs']
print(f'{len(editorials_meta)} editorials found')

if len(editorials_meta) == 0:
    url = f'''https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=pub_date:("{datetime.today().year}-{datetime.today().month}-{datetime.today().day-2}") AND type_of_material:("Editorial")&sort=newest&api-key={nyt_key}'''
    r = requests.get(url)
    editorials_meta = r.json()['response']['docs']
    print(f'{len(editorials_meta)} editorials found')
global paragraph_list
def editorial_content(editorial_url):
    #for url in editorial_urls:
    r = requests.get(editorial_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    article = soup.find_all('section', attrs={'name':'articleBody'})
    print(len(article))
    global paragraph_list
    paragraph_list = article[0].find_all('p')[:-2]
    #print(paragraph_list)
    paragraph_list = [str(p) for p in paragraph_list]
    return ''.join(paragraph_list)

todays_editorials = [dict({'title': editorial['headline']['main'], 'image': f'''https://static01.nyt.com/{editorial['multimedia'][0]['url']}''', 'subtitle': editorial['snippet'], 'article': editorial_content(editorial['web_url'])}) for editorial in editorials_meta]

if not todays_editorials:
    # Show a No editorials found page or read yesterday's editorial
    logging.error('No editorials for today mate')
else:
    formatted_editorials = editorial_formatter(todays_editorials)
    render_editorial(formatted_editorials)

if __name__=='__main__':
    import webbrowser
    rendered_editorials = 'nyt-output.html'
    webbrowser.open_new_tab(rendered_editorials)