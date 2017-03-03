# coding = UTF-8
import codecs
import requests
from bs4 import BeautifulSoup

DownLOAD_URL='https://movie.douban.com/top250'


def download_page(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data= requests.get(url,headers=headers).content
    parse_html(data)
    return data


def parse_html(html):
    movie_name_list=[]
    soup = BeautifulSoup(html)
    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})
    print movie_list_soup
    for movie_li in movie_list_soup.find_all('li'):
        detail_info = movie_li.find('div', attrs={'class': 'item'})
        move_hd = detail_info.find('div', attrs={'class': 'info'})
        move_name = move_hd.find('span', attrs={'class': 'title'}).getText()
        movie_name_list.append(move_name)
    get_next_page=soup.find('div',attrs={'class':'paginator'})
    get_next_url=get_next_page.find('span',attrs={'class':'next'}).find('a')
    if get_next_url:
        return movie_name_list,DownLOAD_URL+get_next_url['href']
    return movie_name_list,None


def main():
    url=DownLOAD_URL
    with codecs.open('movies.txt','wb',encoding='utf-8')as fp:
        while url:
            html=download_page(url)
            movies,url=parse_html(html)
            fp.write(u'{movies}\r\n'.format(movies='\r\n'.join(movies)))


if __name__ == '__main__':
    main()