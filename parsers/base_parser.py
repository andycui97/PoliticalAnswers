from requests import get
from requests.exceptions import RequestException
from contextlib import closing

from bs4 import BeautifulSoup

import re

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    def is_good_response(resp):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200 
                and content_type is not None 
                and content_type.find('html') > -1)

    def log_error(e):
        """
        It is always a good idea to log errors. 
        This function just prints them, but you can
        make it do anything.
        """
        print(e)

    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None




def clean_forms(raw_html_text):
    """
    Returns cleaned raw html by running re.replace on <form> tags.
    Note, the first match is actually only on "<form" and not "<form>"
    Also not that the re.S flag is set to match forms that span multiple lines.   

    Parameters
    ----------
    raw_html_text: text
        Raw html as text. Does not have to be a complete site or even valid html, 
        but is required to have matching sensible <form> tags.

    Returns
    ----------
    res: text
        Cleaned raw html with any forms matching the regex removed.  
    """
    return re.sub('(<form.*?</form>)', '', raw_html_text, flags=re.S)


def clean_scripts(raw_html_text):
    """
    Returns cleaned raw html by running re.replace on <script> tags.
    Note, the first match is actually only on "<script" and not "<script>"
    Also not that the re.S flag is set to match forms that span multiple lines.   

    Parameters
    ----------
    raw_html_text: text
        Raw html as text. Does not have to be a complete site or even valid html, 
        but is required to have matching sensible <script> tags.

    Returns
    ----------
    res: text
        Cleaned raw html with any scripts matching the regex removed.  
    """
    return re.sub('(<script.*?</script>)', '', raw_html_text, flags=re.S)

def remove_header(raw_html_text):
    """
    Returns cleaned raw html by running re.replace on <header> tags.
    Note, the first match is actually only on "<header" and not "<header>"
    Also not that the re.S flag is set to match forms that span multiple lines.   

    Parameters
    ----------
    raw_html_text: text
        Raw html as text. Does not have to be a complete site or even valid html, 
        but is required to have matching sensible <header> tags.

    Returns
    ----------
    res: text
        Cleaned raw html with any headers matching the regex removed.  
    """
    return re.sub('(<header.*?</header>)', '', raw_html_text, flags=re.S)

def remove_head(raw_html_text):
    """
    Returns cleaned raw html by running re.replace on <head> tags.
    Note, the first match is actually only on "<head" and not "<head>"
    Also not that the re.S flag is set to match forms that span multiple lines.   

    Parameters
    ----------
    raw_html_text: text
        Raw html as text. Does not have to be a complete site or even valid html, 
        but is required to have matching sensible <head> tags.

    Returns
    ----------
    res: text
        Cleaned raw html with any heads matching the regex removed.  
    """
    return re.sub('(<head.*?</head>)', '', raw_html_text, flags=re.S)

def remove_footer(raw_html_text):
    """
    Returns cleaned raw html by running re.replace on <footer> tags.
    Note, the first match is actually only on "<footer" and not "<footer>"
    Also not that the re.S flag is set to match forms that span multiple lines.   

    Parameters
    ----------
    raw_html_text: text
        Raw html as text. Does not have to be a complete site or even valid html, 
        but is required to have matching sensible <footer> tags.

    Returns
    ----------
    res: text
        Cleaned raw html with any footers matching the regex removed.  
    """
    return re.sub('(<footer.*?</footer>)', '', raw_html_text, flags=re.S)

def list_links(raw_html_text):
    """
    Returns all links in the raw html provided.

    Parameters
    ----------
    raw_html_text: text
        Raw html as text. Currently requires valid html. TODO: consider changing that

    Returns
    ----------
    res: list
        List of all substrings of the input that match the list regex. 
    """

    parse = BeautifulSoup(raw_html_text)
    links = []
    for link in parse.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))
    return links


def main():
    """
    For testing purposes only
    """
    tmp = simple_get('https://www.congress.gov/roll-call-votes')
    print(tmp)
    links = list_links(tmp)
    print(links)
    
if __name__== "__main__":
  main()
