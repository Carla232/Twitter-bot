import tweepy
import time

consumer_key='1017337919206514689-z9lypN5YIyh2hI6rdBSEDHXyw54gg3'
consumer_secret='tc5lwZULyV1su0yDysoKZdq1b0CjYCIRubSXOli6CbBO1'

key='oDnoahwB5Q0W0oeDYxgtccqxn'
secret='ROpGlh22E6wYB3igGsZpAqCjXESmc79tRLjqrORvr43rG8X57t'

auth = tweepy.OauthHnadler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

FILE_NAME='last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'e')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#ultimatebot' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + "Auto reply, like, and retweet work :)" , tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15)
