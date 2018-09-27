from base_parser import *

def clean_page(raw_html):
    return remove_footer(remove_head(remove_header(clean_scripts(clean_forms(raw_html)))))

def main():
    """
    For testing purposes only
    """
    raw_html = simple_get('https://www.congress.gov/roll-call-votes')
    raw_html_cleaned = clean_page(raw_html.decode("utf-8"))
    print("\n".join(list_links(raw_html_cleaned)))

if __name__== "__main__":
  main()
