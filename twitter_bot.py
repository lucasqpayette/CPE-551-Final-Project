import tweepy
import backend

consumer_key = 'sdf'
consumer_secret = 'sdf'
access_token = 'sdf'
access_token_secret = 'sdf'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)