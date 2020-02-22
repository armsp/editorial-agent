#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

class EditorialGridItem:
    def __init__(self, title, image_url, subtitle, article):
        print('init')
        self.title = title
        self.image = image_url
        self.subtitle = subtitle
        self.article = article
        self.item_div = {"class": "editorial"}
        self.title_div_attr = {"class": "editorial-title"}
        self.image_div_attr = {"class": "editorial-image"}
        self.subtitle_div_attr = {"class": "editorial-subtitle"}
        self.article_div_attr = {"class": "editorial-article"}
        self.item_content = None
        self._soup = BeautifulSoup('', 'html.parser')

    def title_div(self):
        print('title div')
        title_div = self._soup.new_tag('div', attrs=self.title_div_attr)
        title_div.append(self.title)
        self._soup.append(title_div)

    def image_div(self):
        print('img div')
        image_div = self._soup.new_tag('div', attrs=self.image_div_attr)
        image = self._soup.new_tag('img', src=self.image)
        image_div.append(image)
        self._soup.append(image_div)

    def subtitle_div(self):
        print('subtit div')
        subtitle_div = self._soup.new_tag('div', attrs=self.subtitle_div_attr)
        subtitle_div.append(self.subtitle)
        self._soup.append(subtitle_div)

    def article_div(self):
        print('art div')
        article_div = self._soup.new_tag('div', attrs=self.article_div_attr)
        article_div.append(self.article)
        self._soup.append(article_div)

    def form_editorial_item(self):
        self.title_div()
        self.image_div()
        self.subtitle_div()
        self.article_div()
        editorial_item_container = BeautifulSoup('', 'html.parser')
        editorial_item_container_soup = editorial_item_container.new_tag('div', attrs=self.item_div)
        editorial_item_container_soup.append(self._soup)
        editorial_item_container.append(editorial_item_container_soup)
        self.item_content = str(editorial_item_container)

if __name__=='__main__':
    title = "Hello World"
    subtitle = "fuck"
    image_url = "https://gfycat.com/timelynauticalblackfly"
    article = "This si a good article. Don't you agree Mr President? Yeah. But Parasite? It should have been Gone with the Wind!"
    item = EditorialGridItem(title=title, image_url=image_url, subtitle=subtitle, article=article)
    item.form_editorial_item()
    print(item.item_content)

