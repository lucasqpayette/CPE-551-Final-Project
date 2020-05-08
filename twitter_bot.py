import tweepy
import backend
import password

hi_maria = 1 

auth = tweepy.OAuthHandler(password.consumer_key, password.consumer_secret)
auth.set_access_token(password.access_token, password.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline()
for tweet in public_tweets:
    print(tweet.text)