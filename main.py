import pandas as pd
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


data = pd.read_csv('https://gist.githubusercontent.com/hasmanyguitars/232302a4ba29fd8f5f0d0352ef55d2b9/raw/8e2c91bcabd5edd936e06d99de519741e3b7bff8/rolling_stone_top_500_albums_2020.csv', usecols=['Rank', 'Artist', 'Album', 'Description'])
data['link'] = ''
data['image'] = ''
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def get_data():
    for index, row in data.iterrows():
        searchQuery = row['Album'] + ' ' + row['Artist']
        searchResults = spotify.search(searchQuery, 1, 0, 'album')
        if len(searchResults.get('albums').get('items')) != 0:
            data.at[index, 'link'] = searchResults.get('albums').get('items')[0].get('external_urls').get('spotify')
            data.at[index, 'image'] = searchResults.get('albums').get('items')[0].get('images')[0].get('url')

get_data()
with open('data.csv', 'w') as d:
    d.write(data.to_csv(index=False))