import json
import urllib.request
from urllib import parse
from bs4 import BeautifulSoup
from pprint import pprint

def find_code(st):
    buffer = ''
    for c in st[::-1]:
        if c == '=':
            break
        buffer += c
    return int(buffer[::-1])

BASE_URL='https://movie.naver.com/movie/bi/pi/basic.nhn?code='

db = []
code_book, actor_book, director_book = {}, {}, {} #중복 확인을 위한 딕셔너리
files = ['actor_list.json', 'staff_list.json']
for file_name in files:
    with open(file_name, 'rb') as fr:
        person_dic = json.load(fr)

    for name in person_dic:
        link = person_dic[name]
        code = find_code(link)

        # '배우'이면서 '감독'일 경우. 배역을 수정해준다.
        if code in code_book:
            for dic in db:
                if dic['pk'] == code:
                    dic['fields']['role'].append('감독/각본/제작')
                    director_book[code] = 1
                    break
            continue # 다음 이름으로 작업이 넘어간다.

        # 크롤링
        url = BASE_URL + str(code)
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'lxml')

        # 이미지
        img_url = soup.find('div', 'poster').find('img')['src']

        # 설명(프로필에 있을 경우에만 저장)
        description = soup.find('div', 'con_tx')
        if description == None:
            description = '정보 없음'
        else:
            description = description.text

        person = {
            'pk': code,
            'model': 'movies.movier',
            'fields': {
                'name': name,
                'role': [],
                'img_url': img_url,
                'description': description,
            }
        }
        if file_name == 'actor_list.json':
            person['fields']['role'].append('배우')
            actor_book[code] = 1
        else:
            person['fields']['role'].append('감독/각본/제작')
            director_book[code] = 1

        db.append(person)
        code_book[code] = 1
fr.close()

#####################################################################################

# movies.json을 순회하면서, 현재 movier db에 저장되지 않은 사람들을 추가해준다.
SEARCH_BASE_URL_QUERY = 'https://movie.naver.com/movie/search/result.nhn?query='
SEARCH_BASE_URL_OPTION = '&section=people&ie=utf8'


with open('movies.json', 'rb') as fr:
    movie_dic = json.load(fr)

for movie in movie_dic:
    directors = movie['fields']['director']
    actors = movie['fields']['actor']
    newbies = directors + actors # 0~len(directors)-1 | len(directors)~len(actors)-1
    for idx, name in enumerate(newbies):
        # url에 이름을 사용하기 위해서는 한글 인코딩이 필요 (parse.quote())
        url = SEARCH_BASE_URL_QUERY + parse.quote(name) + SEARCH_BASE_URL_OPTION
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'lxml')
        target = soup.find('ul', 'search_list_1')
        if target == None:
            continue
        else:
            link = target.find('a')['href']
        code = find_code(link)

        # 이 인물이 추가된 적이 없을 경우, 추가한다.
        if code not in code_book:
        
            url = BASE_URL + str(code)
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'lxml')

            # 이미지
            img_url = soup.find('div', 'poster').find('img')['src']

            # 설명(프로필에 있을 경우에만 저장)
            description = soup.find('div', 'con_tx')
            if description == None:
                description = '정보 없음'
            else:
                description = description.text

            person = {
                'pk': code,
                'model': 'movies.movier',
                'fields': {
                    'name': name,
                    'role': [],
                    'img_url': img_url,
                    'description': description,
                }
            }
            if idx >= len(directors):
                person['fields']['role'].append('배우')
            else:
                person['fields']['role'].append('감독/각본/제작')

            # print("adding...")
            # pprint(person)
            db.append(person)
            code_book[code] = 1
        
        else:
            # 직업이 여러개인 사람 처리
            if (idx<len(directors)) and (code not in director_book):
                for dic in db:
                    if dic['pk'] == code:
                        dic['fields']['role'].append('감독/각본/제작')
                        director_book[code] = 1
                        break
            elif (idx>=len(directors)) and (code not in actor_book):
                for dic in db:
                    if dic['pk'] == code:
                        dic['fields']['role'].append('배우')
                        actor_book[code] = 1
                        break
                

            # print("done here!")

fr.close()

with open('moviers.json', 'w', encoding='UTF-8-sig') as fp:
    json.dump(db, fp, ensure_ascii=False, indent=4)
fp.close()