from pprint import pprint
import requests


class CountriesWikiLinks:

    def __init__(self, url_dict_json, cursor=-1):
        try:
            response_countries = requests.get(url_dict_json)
        except:
            print('Файл не найден')
        else:
            self.list = response_countries.json()
            self.cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor + 1 >= len(self.list):
            raise StopIteration()
        self.cursor += 1
        return self.list[self.cursor].get('translations').get('rus').get('official')


if __name__ == '__main__':

    url_json = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
    path = 'countriesWikiLinks.txt'
    wiki_ru = 'https://ru.wikipedia.org/wiki/'
    with open(path, 'w', encoding='utf8') as file:
        for country in CountriesWikiLinks(url_json):
            pprint(country)
            file.write(f'{country}\t{wiki_ru + country}\n')
