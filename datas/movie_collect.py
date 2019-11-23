import json
import requests
import urllib.request
from bs4 import BeautifulSoup

def find_tg(st):
    r = len(st)
    tg=''
    idx=0
    for _ in range(r):
        if st[idx] == '"':
            return tg
        tg += st[idx]
        idx += 1


def find_code(st):
    new=int(st[28:])
    return new

def make_lst(st):
    r = len(st)
    idx=0
    new_people=''
    people_lst=[]
    for _ in range(r):
        if st[idx]=='|':
            people_lst.append(new_people)
            new_people=''
        else:
            new_people += st[idx]
        idx+=1
    return people_lst



NAVER_CLIENT_ID='KJX6vxTEIiw5slWc1kuK'
NAVER_SECRET='J7vQdlWbqA'
header={
    "X-Naver-Client-Id":NAVER_CLIENT_ID,
    "X-Naver-Client-secret":NAVER_SECRET,
}
BASE_URL='https://openapi.naver.com/v1/search/movie.json?'
NAVER_URL='https://movie.naver.com/'
IMG_URL='https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode='



with open('checker.json', 'rb') as fr:
    movie_dic = json.load(fr)


db = []
for info in movie_dic:
    k = info['name']
    v = info['link']
    movie={}
    # pk: 영화 코드
    movie['pk'] = find_code(v)
    movie['model']='movies.Movie'

    query_str="query="+k
    req = requests.get(BASE_URL+query_str, headers=header).json()
    tg=req['items']
    if len(tg) > 0:
        new_info=tg[0]

        fields={}
        # 영화 이름
        fields['title'] = new_info['title']

        # 영화 이름(영문)
        fields['title_en'] = new_info['subtitle']

        # 유저 평점
        fields['rate'] = new_info['userRating']
        
        # 영화인리스트 (['이름', '이름'])
        fields['director'] = make_lst(new_info['director'])
        fields['actor'] = make_lst(new_info['actor'])

        # Image URL (api에서 제공하는 url은 크기가 작아서 별도 url사용)
        fields['img_url'] = IMG_URL+str(movie['pk'])

        

        url=NAVER_URL+v
        html=urllib.request.urlopen(url)
        soup=BeautifulSoup(html, 'lxml')

        # 상세설명
        descriptrion = soup.find('div', class_='story_area')
        if descriptrion:
            fields['description'] = descriptrion.p.text
        else:
            fields['description'] = '내용 없음'
        spec = soup.find('dl', class_='info_spec')
        genre=[]
        if spec:
            tg_spec = spec.find('dd')
            spec_links=tg_spec.find_all('a')
            
            for link in spec_links:
                now = str(link)[40:-4]
                new_info = find_tg(now)
                if new_info[:5]=='genre':
                    g = int(new_info[6:])
                    genre.append(g)
                elif new_info[:4]=='open':
                    op = new_info[5:]
                    if len(op) > 5:
                        # 개봉일('yyyymmdd')
                        fields['open_date'] = op

        else:
            fields['open_date'] = '정보 없음'

        # 장르(genre_id list)
        fields['genre'] = genre
        movie['fields'] = fields
        db.append(movie)

with open('movies.json', 'w', encoding='UTF-8-sig') as fp:
    json.dump(db, fp, ensure_ascii=False, indent=4)




''' Test Code

# ex_movie = '캐리비안의 해적 - 블랙 펄의 저주'
# ex_url='/movie/bi/mi/basic.nhn?code=37148'
# ex_code=find_code(ex_url)
    
# s_url='{}{}'.format(NAVER_URL, ex_url)
# html = urllib.request.urlopen(s_url)
# soup = BeautifulSoup(html, 'lxml')

# description = soup.find('div', class_='story_area').p.text

# spec = soup.find('dl', class_='info_spec')
# tg_spec = spec.find('dd')
# spec_links=tg_spec.find_all('a')
# genre=[]
# for link in spec_links:
#     now = str(link)[40:-4]
#     new_info = find_tg(now)
#     if new_info[:5]=='genre':
#         g = int(new_info[6:])
#         genre.append(g)
#     elif new_info[:4]=='open':
#         op = new_info[5:]
#         if len(op) > 5:
#             open_date=op

        
# for title in titles:
#     name = title.find('a').text
#     link = title.find('a')['href']
#     print(link)
#     if name not in db:
#         db[name] = link
#         # print("adding:", name)

'''