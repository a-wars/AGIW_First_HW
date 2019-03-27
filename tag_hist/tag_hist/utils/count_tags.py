from bs4 import BeautifulSoup

def count_tags(html_src):
    soup = BeautifulSoup(html_src, 'html.parser')
    tag_num = len(soup.find_all())
    return tag_num