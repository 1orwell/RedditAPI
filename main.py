import requests
import pandas as pd
from IPython.display import display

subreddit = "knitting"
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

def get_results(r):
    #create DataFrame showing title, url, score and number of comments

    my_dict = {}
    for post in r['data']['children']:
        x = post['data']['title']
        my_dict[x] = {'url':post['data']['url'],'score':post['data']['score'],'comments':post['data']['num_comments']}
    """
    pd stands for pandas - used for data manipulation and analysis
    e.g.
    d = {'col1' : [1, 2], 'col2' : [3, 4]}
    df = pd.DataFrame(data = d)
    >> df
        col1    col2
    0      1       3
    1      2       4
    """
    df = pd.DataFrame.from_dict(my_dict, orient='index')
    return(df)

r = get_reddit(subreddit, listing, limit, timeframe)
df = get_results(r)
display(df.to_string())
#df.to_csv(r'C:\Users\44742\Documents\Programs\Git\RedditAPI', header=None, index=None, sep=' ', mode='a')
df.to_csv('reddit_data.csv')
#posts = get_post_titles(r)