from jinja2 import Environment, FileSystemLoader

template_loader = FileSystemLoader('./templates')
template_env = Environment(loader=template_loader)

TEMPLATE_FILE = "template.html"
template = template_env.get_template(TEMPLATE_FILE)


def render_editorial(editorial_list):
    output_html = template.render(editorials = editorial_list)
    #print(output_html)

    with open("output.html", "w+") as f:
        f.write(output_html)