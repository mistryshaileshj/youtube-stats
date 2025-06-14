import requests
import pandas as pd
import time

API_KEY = "AIzaSyBHrLsTXbO05Kpirk-aQwi1DhA2u0AkbPo"
CHANNEL_ID = "UCl23mvQ3321L7zO6JyzhVmg" #Mumbai Indians
#CHANNEL_ID = "UCb4AW4DtF_iS4_eNuTgEgRA" #Sourav Joshi Vlogs

def get_upload_playlist_id(api_key, channel_id):
    print("starting get_upload_playlist_id...")

    url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={channel_id}&key={api_key}"
    print(f"api url: {url}")
    
    r = requests.get(url).json()
    return r['items'][0]['contentDetails']['relatedPlaylists']['uploads']

def get_all_video_ids(api_key, upload_playlist_id, max_videos=10000):
    print("starting get_all_video_ids...")
    
    video_ids = []
    next_page_token = None

    print("starting video id loop")
    while len(video_ids) < max_videos:
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={upload_playlist_id}&maxResults=50&pageToken={next_page_token or ''}&key={api_key}"
        r = requests.get(url).json()
        for item in r['items']:
            video_ids.append(item['contentDetails']['videoId'])

        next_page_token = r.get('nextPageToken')
        if not next_page_token:
            break

        time.sleep(0.1)  # be nice to the API

    return video_ids

def get_video_stats(api_key, video_ids):
    print("starting get_video_stats...")
    
    all_data = []

    print("starting video stats loop")
    for i in range(0, len(video_ids), 50):
        ids_chunk = ",".join(video_ids[i:i+50])
        url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={ids_chunk}&key={api_key}"
        r = requests.get(url).json()

        for item in r['items']:
            data = {
                "video_id": item['id'],
                "title": item['snippet']['title'],
                "published_at": item['snippet']['publishedAt'],
                "views": item['statistics'].get('viewCount', 0),
                "likes": item['statistics'].get('likeCount', 0),
                "comments": item['statistics'].get('commentCount', 0)
            }
            all_data.append(data)

        time.sleep(0.1)

    return pd.DataFrame(all_data)

# Run the fetch
upload_playlist_id = get_upload_playlist_id(API_KEY, CHANNEL_ID)
video_ids = get_all_video_ids(API_KEY, upload_playlist_id, max_videos=10000)
df = get_video_stats(API_KEY, video_ids)

cnt = len(df)
print(f"dataframe rows: {cnt}")

# Save to CSV
csv_file = "s3://consolidated-bucket-for-allprojects/USA-Branch-Reporting-UCOA/mumind_youtube_video_stats.csv"
df.to_csv(csv_file, index=False)
print(f"Saved {len(df)} videos to {csv_file}")
