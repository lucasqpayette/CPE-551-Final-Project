import tweepy
import backend
import password

auth = tweepy.OAuthHandler(password.consumer_key, password.consumer_secret)
auth.set_access_token(password.access_token, password.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.mentions_timeline()
last_tweet = public_tweets[0].text
last_tweet = last_tweet.split(' ')

print(last_tweet[1])

for tweet in last_tweet:
    if tweet == 'hello':
        print(1)
    else:
        print(2)
    # print(tweet.text)