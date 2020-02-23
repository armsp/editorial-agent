from bs4 import BeautifulSoup
from highlighter import highlight

def editorial_formatter(editorial_list):
    formatted_editorials = []
    for editorial_dict in editorial_list:
        #highlight
        editorial_article = editorial_dict['article']
        article_soup = BeautifulSoup(editorial_article, 'html.parser')
        p_elements = article_soup.find_all('p')
        highlighted_p_elements = highlight(p_elements)
        formatted_editorial_dict = {'article': highlighted_p_elements, 'title': editorial_dict['title'], 'image': editorial_dict['image'], 'subtitle': editorial_dict['subtitle']}
        formatted_editorials.append(formatted_editorial_dict)
    return formatted_editorials




