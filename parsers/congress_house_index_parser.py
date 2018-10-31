from base_parser import *

def clean_main_page(raw_html):
    for tag in ['script', 'form', 'footer', 'head', 'header']:
        raw_html = remove_type_of_tag(raw_html, tag)
    return raw_html

def clean_list_pages(raw_html):
    for tag in ['script', 'form', 'footer', 'head', 'header', 'style']:
        raw_html = remove_type_of_tag(raw_html, tag)
    return raw_html

def main():
    """
    For testing purposes only
    """
    raw_html = simple_get('https://www.congress.gov/roll-call-votes')
    raw_html_cleaned = clean_main_page(raw_html.decode("utf-8"))
    roll_call_links = list_links(raw_html_cleaned)
    for link in roll_call_links:
        if link.startswith('http://www.senate.gov/'):
            link_raw_html = simple_get(link).decode("utf-8")
            link_raw_html = clean_list_pages(link_raw_html)
            get_first_table(link_raw_html)

if __name__== "__main__":
  main()
