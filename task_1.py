
import requests
from urllib.parse import quote
import data as d


class Wiki_country:
    def __init__(self, url: str):
        self.url = url

    def __iter__(self):
        self.response = requests.get(self.url, stream=True)
        self.response_lines = self.response.iter_lines(decode_unicode=True)
        return self.response_lines

    def info_dict(self):
        new_dict = {}
        for line in self:
            if line[0:d.cut] == d.marked_line:
                decoded = line[d.cut:-2].encode('utf-8').decode('unicode-escape')
                link = 'https://en.wikipedia.org/wiki/{0}'.format(quote(decoded))
                new_dict[decoded] = link
        return new_dict

    def make_file(self):
        with open('wiki_links.txt', 'w', encoding='utf-8') as file:
            for key, val in self.info_dict().items():
                file.write('{}: {}\n'.format(key,val))


if __name__ == '__main__':
    countries = Wiki_country(d.URL)
    countries.make_file()


