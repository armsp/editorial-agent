#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:10:05 2020

@author: walker
"""
from bs4 import BeautifulSoup

title = "Hello World"
subtitle = "fuck"
image_url = "https://gfycat.com/timelynauticalblackfly"
article = "This si a good article. Don't you agree Mr President? Yeah. But Parasite? It should have been Gone with the Wind!"

# you form your html independent of the template
# once your html is ready, you just convert it to text and put it in the {content} of template
editorial_container = BeautifulSoup('', 'html.parser')
editorial_container_soup = editorial_container.new_tag('div', attrs={"class": "editorial"})

editorial_soup = BeautifulSoup('', 'html.parser')

editorial_title = editorial_soup.new_tag('div', attrs={"class": "editorial-title"})
editorial_image = editorial_soup.new_tag('div', attrs={"class": "editorial-image"})
image = editorial_soup.new_tag('iframe', src=image_url)
editorial_subtitle = editorial_soup.new_tag('div', attrs={"class": "editorial-subtitle"})
editorial_article = editorial_soup.new_tag('div', attrs={"class": "editorial-article"})

editorial_title.append(title)
editorial_image.append(image)
editorial_subtitle.append(subtitle)
editorial_article.append(article)

editorial_soup.append(editorial_title)
editorial_soup.append(editorial_image)
editorial_soup.append(editorial_subtitle)
editorial_soup.append(editorial_article)

editorial_container_soup.append(editorial_soup)
editorial_container.append(editorial_container_soup)
print(editorial_container.prettify())
print(''' ---------------------------------------------------------------------------------------------- ''')

#editorial_title_soup = BeautifulSoup('', 'html.parser')
#editorial_subtitle_soup = BeautifulSoup('', 'html.parser')
#editorial_image_soup = BeautifulSoup('', 'html.parser')
#editorial_text_soup = BeautifulSoup('', 'html.parser')

contents = editorial_container

with open('template.html') as f:
    template_string = f.read()

print(template_string.format(content=str(contents)))

with open('output123.htm', 'w+') as f:
    f.write(template_string.format(content=str(contents)))



