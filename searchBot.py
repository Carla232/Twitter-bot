import tweepy
import time

consumer_key='1017337919206514689-z9lypN5YIyh2hI6rdBSEDHXyw54gg3'
consumer_secret='tc5lwZULyV1su0yDysoKZdq1b0CjYCIRubSXOli6CbBO1'

key='oDnoahwB5Q0W0oeDYxgtccqxn'
secret='ROpGlh22E6wYB3igGsZpAqCjXESmc79tRLjqrORvr43rG8X57t'

auth = tweepy.OauthHnadler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = "#TheHunt"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchBot()
