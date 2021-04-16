import praw
import datetime as dt
import re


reddit = praw.Reddit(client_id='CLIENT_ID',
                     client_secret='CLIENT_SECRET',
                     user_agent='NAME_OF_APPLICATION',
                     username='REDDIT_USERNAME',
                     password='REDDIT_PASSWORD')


subreddit = reddit.subreddit('CryptoMoonShots')

top_subreddit = subreddit.top()


cryptoRegex = '[$][a-zA-Z]+'
cryptoDict = {}
for x in top_subreddit:

    # getting all cryptos from title and body
    cryptosTitle = re.findall(cryptoRegex, x.title)
    cryptosBody = re.findall(cryptoRegex, x.selftext)
    cryptos = cryptosTitle + cryptosBody

    # formatting date
    cryptoDateTime = str(dt.datetime.fromtimestamp(x.created))
    if cryptos:
        # removing duplicates because it is mentioned on same time will reduce our time managing dictionary
        cryptos = list(dict.fromkeys(cryptos))
        # print(cryptos)
        # print(cryptoDateTime)
        for crypto in cryptos:
            # converting to upper case
            crypto = crypto.upper()
            # removing $
            crypto = crypto[1:]
            if crypto in cryptoDict.keys():
                cryptoDict[crypto].append(cryptoDateTime)
            else:
                cryptoDict[crypto] = []
                cryptoDict[crypto].append(cryptoDateTime)


print(cryptoDict)
