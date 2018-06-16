from html.parser import HTMLParser
from urllib import parse


class LinkDetector(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    ''' Here we dont care about end tag.. What i meant o say is
    consider this basic html template
    <body>
        <a href='www.google.com'>Google </a>
        now we dont care here about the end tag. What we do care about is the link, and we can find that by exploring the start tags'''

    def handle_starttag(self, tag, attrs):  # Overriden
        if tag == 'a':  # Since links are only present in the anchor tag
            for (attribute, value) in attrs:  # attribute is for example href and value is the url inside it
                if attribute == 'href':
                    # This is also hadling the case of relative url inside html tags
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    # I do need to implemet error here, just checking what happens if I do not define error method here.
    def error(self, message):
        pass
