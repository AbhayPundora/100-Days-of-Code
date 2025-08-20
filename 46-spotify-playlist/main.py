import json
from pprint import pprint

import os
from bs4 import BeautifulSoup
import lxml
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import loadenv

loadenv()

BILLBOARD_ENDPOINT = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_ENDPOINT = "https://api.spotify.com/v1/users/"
OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECTED_URI = os.getenv("REDIRECTED_URI")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope = "playlist-modify-private",
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        redirect_uri = REDIRECTED_URI,
        show_dialog=True,
        cache_path="token.txt",
        username="abhay"
    )
)

user_id = sp.current_user()["id"]
# print(user_id)

headers = {"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}


user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

try:
    response = requests.get(url=f"{BILLBOARD_ENDPOINT}{user_date}")

except FileNotFoundError:
    print("Enter valid date")

except ConnectionError:
    print("No Internet Connection")

else:
    contents = response.text
    soup = BeautifulSoup(contents, "lxml")
    # print(soup)

    songs_tag_list = soup.select(selector="li ul li h3")

    songs = [tag.getText().strip() for tag in songs_tag_list]
    year = user_date.split("-")[0]

    song_URIs = []

    for song in songs:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        # print(json.dumps(result))
        try:
            uri = result["tracks"]["items"][0]["uri"]
        except IndexError:
            print(f"{song} is not available")

        else:
            song_URIs.append(uri)

    # print(song_URIs)

    # body = {
    #     "name": f"{user_date} Billboard 100",
    #     "description": "just for fun",
    #     "public": False
    # }
    #
    # headers = {
    #     "Authorization": f"Bearer {ACCESS_TOKEN}"
    # }
    #
    # response = requests.post(url=f"{SPOTIFY_ENDPOINT}{user_id}/playlists", json=body, headers=headers)
    # print(response.text)

    # playlist_id = "6V64OuM9KWfQP11CyQgJRp"

    # for i in range(0, len(song_URIs)):
    #     body = {
    #         "uris": [
    #             song_URIs[i]
    #             ],
    #         "position": i
    #     }
    #     response = requests.post(url=f"{SPOTIFY_ENDPOINT}{playlist_id}tracks", json=body, headers=headers)

    playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)
    # print(playlist)

    sp.playlist_add_items(playlist_id=playlist["id"], items=song_URIs)
