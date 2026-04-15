from ytmusicapi import YTMusic

def search_youtube_music(search_query="new hindi song",
                         filter="songs",
                           limit=100):
    
    ytmusic = YTMusic()

    search_results = ytmusic.search(search_query, filter=filter, limit=limit)


    valid_tracks = []

    for track in search_results:
        track_name = track['title']
        
        artists = track.get('artists', [])
        artist_name = artists[0]['name'] if artists else ""
        track_info = {"track_name": track_name, "artist": artist_name,"duration": track.get('duration_seconds'), 'views': track.get('views')}
        if track_info not in valid_tracks:
            valid_tracks.append(track_info)

        print(f"Found track: '{track_name}' by '{artist_name}' with duration {track.get('duration_seconds')} seconds and {track.get('views')} views")

    return valid_tracks

if __name__ == "__main__":
    search_youtube_music()