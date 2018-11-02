#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import bs4

def url2soup(url, headers={}, data=None):
    # url -> soup
    if data:
        response = requests.post(url, data=data, headers=headers)
    else:
        response = requests.get(url, headers=headers)
    # response.encoding == 'ISO-8859-1':
    encodings = requests.utils.get_encodings_from_content(response.text)
    if encodings:
        encoding = encodings[0]
    else:
        encoding = response.apparent_encoding
    encode_content = response.content.decode(encoding, 'replace')
    return bs4.BeautifulSoup(encode_content, "lxml")


class Crawler(object):
    '''[Summary for Class Crawler]Crawler has 2 (principal) propteries
    url: url
    tag: tag [None]
    '''
    def __init__(self, url, tag='body'):
        self.url = url
        self.tag = tag
        self.open = []
        self.closed = []

    def parse(self, *args, **kwargs):
        self.__soup = url2soup(self.url, *args, **kwargs)

    @property
    def soup(self):
        return self.__soup
    
    def get_urls(self, check=True):
        tag = self.soup
        if self.tag:
            tag = self.soup.find(self.tag)
        urls = []
        for a in tag.find_all('a'):
            if a.has_attr('href'):
                url = a['href']
                if url != '/' and url != self.url:
                    if check and check(url):
                        urls.append(url if url.startswith('http') else self.url + url)
        return urls


    def find(self, *args, **kwargs):
        tag = self.soup
        if self.tag:
            tag = soup.find(tag)
        return tag.find(*args, **kwargs)

    def find_all(self, *args, **kwargs):
        tag = self.soup
        if self.tag:
            tag = soup.find(tag)
        return tag.find_all(*args, **kwargs)

    def search(self, check=None, *args, **kwargs):

        from simpleai.search import SearchProblem, astar

        class Problem(SearchProblem):

            def actions(self, state):
                pass

            def result(self, url, *args):
                soup = url2soup(url)
                return [a['href'] if a['href'].startswith('http') else self.url + a['href'] for a in tag.find_all('a') \
                 if a.has_attr('href') and a['href'] != '/' and a['href'] != url]

            def is_goal(self, url):
                if check is None or check(url):
                    soup = url2soup(url)
                    a = soup.find(*args, **kwargs)
                if a:
                    self.result = a
                    return True
                else:
                    return False

            def state_representation(self, url):
                return 'URL = ' + url

            problem = Problem(initial_state=self.url)

            result = astar(problem)


if __name__ == '__main__':
    # test
    c = Crawler(url='https://blog.csdn.net')
    c.parse()

    import re
    rx = re.compile(r'.+/\d+\Z')
    def check(url):
        return rx.match(url)

    for url in c.get_urls(check):
        print(url)

