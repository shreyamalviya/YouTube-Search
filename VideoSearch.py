import fire
from apiclient.discovery import build

DEVELOPER_KEY = "AIzaSyAWUOavwzBsnKCeia2M1aqmpG40O2v0ZZk"
YT_API_SERVICE_NAME = "youtube"
YT_API_VERSION = "v3"

YT = build(YT_API_SERVICE_NAME, YT_API_VERSION,
           developerKey=DEVELOPER_KEY)

maxResults = 10


def YTsearch(searchString=None):
    if searchString:
        search = YT.search().list(q=searchString,
                                  part='id, snippet',
                                  maxResults=maxResults,
                                  type='video').execute()

        results = search.get("items", [])

        videos = []

        for result in results:
            videos.extend(["\033[95m\033[1m\033[4m" + result['snippet']['title'] + "\033[0m",
                           "\033[94mhttps://www.youtube.com/watch?v=" +
                           result['id']['videoId'] + "\033[0m",
                           result['snippet']['description'],
                           "\n"])

        print("\n", "\n".join(videos))

    else:
        print("\n\033[91m\033[1mSearch box can not be empty. Try again!\n")


if __name__ == "__main__":
    fire.Fire(YTsearch)
