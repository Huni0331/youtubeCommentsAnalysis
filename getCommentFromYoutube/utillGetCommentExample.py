# 1. File name utillGetCommentExample.py -> utillGetComment.py
# 2. pip install google-api-python-client



from googleapiclient.discovery import build # 2. pip install google-api-python-client


YOUTUBE_API_KEY = "YOUR_YOUTUBE_API"


def getComments(urlvalue):
    DEVELOPER_KEY = YOUTUBE_API_KEY
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    reviews = []
    npt = ""
    videoId_init = urlvalue
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    cm = youtube.commentThreads().list(
        videoId=videoId_init,  # ioB-Tr7Qt6g(key 있음) # NLl5tx9Ce00(key 없음)
        order="relevance",
        part="snippet",
        maxResults=100,
        pageToken=npt
    ).execute()

    if 'nextPageToken' in cm.keys():
        while 'nextPageToken' in cm.keys():
            cm = youtube.commentThreads().list(
                videoId=urlvalue,
                order="relevance",
                part="snippet",
                maxResults=100,
                pageToken=npt
            ).execute()
            for i in cm['items']:
                reviews.append(i['snippet']['topLevelComment']['snippet']['textOriginal'])

            if 'nextPageToken' in cm.keys():
                npt = cm['nextPageToken']
            else:
                break
    else:
        for i in cm['items']:
            reviews.append(i['snippet']['topLevelComment']['snippet']['textOriginal'])

    return reviews


def getThumbnail(urlvalue):
    DEVELOPER_KEY = YOUTUBE_API_KEY
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    titles = []
    images = []
    npt = ""
    videoId_init = urlvalue
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    cm = youtube.videos().list(
        id=videoId_init,
        part='snippet'
    ).execute()


    for i in cm['items']:
        titles.append(i['snippet']['title'])
        images.append(i['snippet']['thumbnails']['medium']['url'])

    return titles, images
