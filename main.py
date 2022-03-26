import requests

subreddit = "python"
listing = "top" # controversial, best, hot, new, etc.
limit = 100
timeframe = "month" #hour, day week, month, day, year, all

from webbrowser import get
def get_reddit(subreddit, listing, limit, timeframe):
    try:
        base_url = f"https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}"
        request = requests.get(base_url, headers = {"User-agent" : "yourbot"})
    except:
        print("An error occured")
    return request.json()

def get_post_titles(r):
    # get a list of post titles
    posts = []
    for post in r['data']['children']:
        x = post['data']['title']
        posts.append(x)
    return posts

r = get_reddit(subreddit, listing, limit, timeframe)
posts = get_post_titles(r)
print(posts)