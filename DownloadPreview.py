import yt_dlp
from pydub import AudioSegment

def download_track(metadata, download_path="./downloads", trim_duration=30, trim_start=0):
    """
    Given a track's metadata, search YouTube for the best match and download the audio preview.
    """

    search_query = f"{metadata['artist']} - {metadata['track']} audio"

    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'outtmpl': f'{download_path}/{search_query}.%(ext)s', # Saves the file with the YouTube video title
    'noplaylist': True,
    'quiet': False}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Searching YouTube for: {search_query}...")
        # 'ytsearch1:' tells it to just grab the top 1 result
        ydl.download([f"ytsearch1:{search_query}"])
        print(f"Download complete for {search_query}")

    trim(file_path=f'{download_path}/{search_query}.wav', start_time=trim_start, duration=trim_duration)



def trim(file_path, start_time=0, duration=30):
    """
    Trims the audio file to the specified duration starting from start_time.
    """
    
    audio = AudioSegment.from_file(file_path)
    trimmed_audio = audio[start_time*1000:(start_time+duration)*1000]  # pydub works in milliseconds
    trimmed_audio.export(file_path, format="wav")