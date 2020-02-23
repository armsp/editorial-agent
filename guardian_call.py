import os
import logging
from datetime import datetime

import yaml
import requests

from render import render_editorial
from formatter import editorial_formatter

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')
guardian_endpoint = '''https://content.guardianapis.com/tone/editorials'''

with open('.secrets.yaml') as f:
    secrets = yaml.safe_load(f)

guardian_key = secrets['GUARDIAN-KEY']
guardian_payload = {'show-fields': 'body', 'api-key': guardian_key}

r = requests.get(guardian_endpoint, params=guardian_payload)
logging.debug(f"Response status: {r.status_code}")

if r.status_code != requests.codes.ok:#r.status != 200:
    logging.debug("No response, Aborting...")
    exit()

response_json = r.json()
top_10_editorials = response_json['response']['results']
# convert your local time to the api's time response format - uTC?

todays_editorials = []
for editorial in top_10_editorials:
    editorial_date = datetime.strptime(editorial['webPublicationDate'], '%Y-%m-%dT%H:%M:%SZ')
    logging.debug(f"Editorial Date: {editorial_date}")
    if editorial_date.day == datetime.today().day or editorial_date.day == datetime.today().day-1:
        editorial_dict = {'title': editorial['webTitle'].split('|')[0].strip(), 'image': None, 'subtitle': None, 'article': editorial['fields']['body']}
        todays_editorials.append(editorial_dict)

if not todays_editorials:
    # Show a No editorials found page or read yesterday's editorial
    logging.error('No editorials for today mate')
else:
    formatted_editorials = editorial_formatter(todays_editorials)
    render_editorial(formatted_editorials)

if __name__=='__main__':
    import webbrowser
    rendered_editorials = 'output.html'
    webbrowser.open_new_tab(rendered_editorials)


