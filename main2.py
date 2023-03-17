import requests
from bs4 import BeautifulSoup



def get_html(URL): 
    # Делать запрос по ссылке и возвращать html код этой страницы
    response = requests.get(URL)
    return response.text

def get_posts_links(html):
    soup = BeautifulSoup(html, "html.parser")
    content = soup.find("div", {"class":"content-wrapper"})
    main = content.find("div", {"class":"main-content"})
    listings = main.find("div", {"class":"listings-wrapper"})
    posts = listings.find_all("div", {"class":"list-item"})
    print(posts)


def main():
    URL = "https://www.bazar.kg/kyrgyzstan/elektronika/kompyutery/noutbuki"
    html = get_html(URL)
    post_links = get_posts_links(html)

if __name__=="__main__":
    main()