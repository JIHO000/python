from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from yt_to_mp3 import get_mp3

DEVELOPER_KEY = "AIzaSyDuyG82_-TrNKoONkr7lTXYvgWcy_ZnMyc"
YOUTUBE_API_SERVICE_NAME="youtube"
YOUTUBE_API_VERSION="v3"
youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

def extract_url(song):
    search_response = youtube.search().list(
        q = song,
        part = "snippet",
        maxResults = 3
        ).execute()

    id = []
    view = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            id.append("%s" % (search_result["id"]["videoId"]))
            request = youtube.videos().list(part='statistics', id=search_result["id"]["videoId"])
            response = request.execute()
            view.append(response['items'][0]['statistics']['viewCount'])
                    
    max_view = max(view)
    max_view_idx = view.index(max_view)

    URL = f"https://www.youtube.com/watch?v={id[max_view_idx]}"
    return [URL, id]

def get_MV(id, rank):
    html_text = """
        <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <iframe
                id="ytplayer"
                type="text/html"
                width="720"
                height="405"
                src=f"https://www.youtube.com/embed/{id}"
                frameborder="0"
                allowfullscreen="allowfullscreen"></iframe>
        </body>
    </html>
    """
    html = "MV/" + str(rank) + ".html"
    html_file = open(html, 'w')
    html_file.write(html_text)
    html_file.close()
    print("succes html")

def get_data(songs):
    for i in range(2):
        URL = extract_url(songs[i]["곡"])
        get_mp3(URL[0])
        get_MV(URL[1], i+1)
