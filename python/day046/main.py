import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
SPOTIFY_ID = os.environ['SPOTIFY_ID']
SPOTIFY_SECRET = os.environ['SPOTIFY_SECRET']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               ))

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]

URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
response.raise_for_status()
songs_web_page = response.text

soup = BeautifulSoup(songs_web_page, "html.parser")
songs_divs = soup.find_all(name="div", class_="o-chart-results-list-row-container")

songs_arr = []
song_uris = []

# Generate array with song title and artist
for song in songs_divs:
    parent = song.find_next(name="h3", id="title-of-a-story", class_="c-title").find_parent()

    title = song.find_next(name="li", class_="o-chart-results-list__item") \
        .find_next(id="title-of-a-story") \
        .getText(strip=True)
    artist = parent.find_next(name="span", class_="c-label").getText(strip=True)
    songs_arr.append({"title": title, "artist": artist})

# Create list of songs
for song in songs_arr:
    result = sp.search(q=f"track:{song['title']} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
