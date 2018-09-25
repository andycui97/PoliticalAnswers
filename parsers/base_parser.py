from requests import get
from requests.exceptions import RequestException
from contextlib import closing

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


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

def clean_forms():
    """
    TODO: clean away everything in a <form></form>
    """
    pass

def clean_scripts():
    """
    TODO: clean away everything in a <script></script>
    """
    pass

def grab_body_highest_header():
    """
    TODO: grab all content below the highest <h*> header in the 
    """
    pass

def main():
    """
    For testing purposes only
    """
    print(simple_get('https://www.congress.gov/roll-call-votes'))
  
def list_links(raw_html_text):
    """
    Returns all links in the raw html provided by running re.findall on <li> tags.  

    Parameters
    ----------
    raw_html_text: text
        Raw html as text. Does not have to be a complete site or even valid html. 

    Returns
    ----------
    res: list
        List of all substrings of the input that match the list regex. 
    """

    return re.findall('<li>.*</li>', raw_html_text)


if __name__== "__main__":
  main()
