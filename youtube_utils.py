import webbrowser
import re
from urllib.parse import urlparse, parse_qs 
from datetime import datetime

from constants.personal_videos_list import videos_list

# Get the current date and time
current_datetime = datetime.now()

# Format the datetime object to get the full weekdayname
today = current_datetime.strftime("%A").lower()

def make_my_personal_playlist_url() -> str:
    
    videos_by_day = {e['day'].lower(): e['videos'] for e in videos_list}
    
    today_videos = videos_by_day.get(today, [])
    videos_ids = []
    
    # Extract JUST the IDs
    for url in today_videos:
        vid = extract_id(url)
        if vid:
            videos_ids.append(vid)
        
        else:
            print(f"⚠️ could not parse video ID from “{url}”")
            
    if not videos_ids:
        raise RuntimeError("No valid video IDs found for today!")
        
    # join 'em  then hit the special endpoint
    joined = ",".join(videos_ids)
    
    return f"https://www.youtube.com/watch_videos?video_ids={joined}&autoplay=1"

def open_personal_playlist():
    
    url = make_my_personal_playlist_url()
    print("Opening playlist URL: ", url)
    
    webbrowser.open(url)

def open_playlist(urls: str | list):
    if isinstance(urls, list):
        url = make_playlist_url(urls)
        webbrowser.open(url)
    
    else:
        webbrowser.open(url + "?autoplay=1")

def make_playlist_url(video_ids: list[str]) -> str:
    # join 'em  then hit the special endpoint
    joined = ",".join(video_ids)
    
    return f"https://www.youtube.com/watch_videos?video_ids={joined}&autoplay=1"

def extract_id(token: str) -> str | None:
    # URL
    try:
        parsed = urlparse(token)
        hostname = parsed.hostname or ""
        
        # youtu.be short links
        if hostname.endswith("youtu.be"):
            return parsed.path.lstrip("/")
        
        # full youtube.com URLs
        if "youtube" in hostname:
            qs = parse_qs(parsed.query)
        
        
        if 'v' in qs:
            return qs["v"][0]
    except:
        pass
        
    # Fallback: if they passed something that *looks* like an ID (11 chars, alnum-_)
    m = re.match(r'^[\w-]{11}$', token)
    return m.group(0) if m else None 

def inform_videos_urls():
      raw = input("Type the list of videos: ")
      tokens = [t.strip() for t in raw.split(",")]

      ids = [vid for vid in (extract_id(t) for t in tokens) if vid]

      if not ids:
            print("No valid videos IDs found!")
      else:
            open_playlist(ids)
