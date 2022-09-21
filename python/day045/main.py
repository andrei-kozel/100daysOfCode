import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
data = requests.get(URL)
movies_web_page = data.text

soup = BeautifulSoup(movies_web_page, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")
rev_movie_titles = list(reversed(movie_titles))
for title in rev_movie_titles:
    title_text = title.getText()
    print(title_text)
