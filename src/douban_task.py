import requests
import aiohttp
from bs4 import BeautifulSoup


def main():
    url = 'https://movie.douban.com/cinema/later/beijing/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko)\
          Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
    }

    response = requests.get(url, headers=headers).content

    # print('response: {}'.format(response))
    init_soup = BeautifulSoup(response, 'lxml')

    all_movies = init_soup.find('div', id='showing-soon')

    # print('all_movies: {}'.format(all_movies))

    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        # print('all_a_tag: {}'.format(all_a_tag))
        # print('all_li_tag: {}'.format(all_li_tag))

        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        response_item = requests.get(url_to_fetch, headers=headers).content
        soup_item = BeautifulSoup(response_item, 'lxml')
        img_tag = soup_item.find('img')
        # print('img_tag: {}, response_item: {}'.format(img_tag, response_item))
        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))


main()
