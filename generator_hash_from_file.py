import hashlib


def generator_hash(path_file):
    with open(path_file, 'r', encoding='utf8') as file:
        for line in file:
            yield hashlib.md5(line.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    path = 'countriesWikiLinks.txt'
    gh = generator_hash(path)
    # print(gh.__next__())
    for string in gh:
        print(string)

