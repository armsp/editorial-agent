#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader

template_loader = FileSystemLoader('./')
template_env = Environment(loader=template_loader)

TEMPLATE_FILE = "temp.html"
template = template_env.get_template(TEMPLATE_FILE)


editorials = [{'title': 'A', 'image': 'i', 'subtitle': 'a', 'article': 'hello'}, {'title': 'B', 'image': 'ii', 'subtitle': 'b', 'article': 'world'}, {'title': 'C', 'image': 'iii', 'subtitle': 'c', 'article': 'end'}]

output_html = template.render(editorials = editorials)

print(output_html)

#with open("output.html", "w+") as f:
#    f.write(output_html)