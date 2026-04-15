import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

from DownloadPreview import download_track


load_dotenv()

scope = ["user-library-read","user-read-recently-played"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_recently_played(limit=50)


for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
    download_track({
        "artist": track['artists'][0]['name'],
        "track": track['name'],},
        trim_start=15, # Start the preview at 15 seconds in
        trim_duration=30 # Make the preview 30 seconds long
    )