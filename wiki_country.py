from pprint import pprint
import requests

# URL_COUNTRIES_JSON = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
# response_countries = requests.get(URL_COUNTRIES_JSON)
# list_countries = response_countries.json()
#
# for item in list_countries:
#     print(item.get('translations').get('rus').get('official'))


class CountriesWikiLinks:

    def __init__(self, url_dict_json):
        response_countries = requests.get(url_dict_json)
        self.list_countries = response_countries.json()

    def __iter__(self):
        return self.list_countries.__iter__()

    def __next__(self):
        item = self.__iter__().__next__()
        if not item:
            raise StopIteration
        # не возвращает из словаря название на русском языке (юникод):
        # return item.get('translations').get('rus').get('official')
        # не возвращает даже тип:
        # return type(item)
        # в обоих return'ах работает так:
        # return item
        # то есть возвращает целиком объект-словарь
        # плюс работает вообще без return'а
        # отчаяние :(
        # а если без генератора (строки с 4 по 9), то прекрасно всё работает :(


if __name__ == '__main__':

    url_json = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
    path = 'countriesWikiLinks.txt'
    wiki_ru = 'https://ru.wikipedia.org/wiki/'
    with open(path, 'w', encoding='utf8') as file:
        for country in CountriesWikiLinks(url_json):
            # хотелось бы, что б в country было только название страны:
            # pprint(country)
            # но в country целиком объект, поэтому название страны приходится доставать здесь:
            data = country.get('translations').get('rus').get('official')
            # еще один косяк - в файле ссылка не клеится ни через join, ни через + :
            file.write(f'{data}\t{wiki_ru + data}\n')
            print(data)
