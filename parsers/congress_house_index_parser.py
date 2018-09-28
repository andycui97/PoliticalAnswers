from base_parser import simple_get, grab_body_highest_header
import re


def main():
    """
    For testing purposes only
    """
    raw_html = simple_get('https://www.congress.gov/roll-call-votes')
    print(raw_html.decode("utf-8"))

if __name__== "__main__":
  main()
