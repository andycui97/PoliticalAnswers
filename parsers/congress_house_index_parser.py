from base_parser import *

def clean_page(raw_html):
    for tag in ['head', 'header', 'footer', 'form', 'script']:
        raw_html = remove_type_of_tag(raw_html, tag)

    return raw_html

def main():
    """
    For testing purposes only
    """
    raw_html = simple_get('https://www.congress.gov/roll-call-votes')
    raw_html_cleaned = clean_page(raw_html.decode("utf-8"))
    print("\n".join(list_links(raw_html_cleaned)))

if __name__== "__main__":
  main()
