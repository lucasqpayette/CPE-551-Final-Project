import tweepy
import backend
import password
import time

auth = tweepy.OAuthHandler(password.consumer_key, password.consumer_secret)
auth.set_access_token(password.access_token, password.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.mentions_timeline()
last_tweet = public_tweets[0].text
last_id = public_tweets[0].id
last_tweet = last_tweet.split(' ')

while True:
    temp_tweet = api.mentions_timeline()
    temp_id = temp_tweet[0].id
    temp_text = temp_tweet[0].text
    temp_text = temp_text.split(' ')
    
    if(temp_id != last_id):
        #tweets should have syntax of @bot, ticker, function
        last_id = temp_id
        ticker = temp_text[1]
        function = temp_text[2]
        if(function == 'price' or function == 'Price'):
            try:
                temp_data = backend.get_price(ticker, 1, password.TS)
                reply='Price: $' + str(temp_data[0])
                api.update_status(reply, in_reply_to_status_id = temp_id, auto_populate_reply_metadata = True)
                print(temp_data)
            except ValueError:
                api.update_status('Invalid Ticker', in_reply_to_status_id = temp_id, auto_populate_reply_metadata = True)
                print('invalid ticker')
        elif(function == "macd" or function == "MACD"):
            try:
                temp_data = backend.MACD(ticker, 1, password.TS)
                temp_string = str(temp_data[0])
                temp_string = temp_string[1:-1]
                reply = 'MACD: $' + temp_string
                api.update_status(reply, in_reply_to_status_id = temp_id, auto_populate_reply_metadata = True)
                print(temp_data)
            except ValueError:
                api.update_status('Invalid Ticker', in_reply_to_status_id = temp_id, auto_populate_reply_metadata = True)
                print('invalid ticker')
        elif(function == 'rsi' or function == "RSI"):
            try:
                temp_data = backend.RSI(ticker, 1, password.TS)
                temp_string = str(temp_data[0])
                temp_string = temp_string[1:-1]
                reply='RSI: $' +  temp_string
                api.update_status(reply, in_reply_to_status_id = temp_id, auto_populate_reply_metadata = True)
                print(temp_data)
            except ValueError:
                api.update_status('Invalid Ticker', in_reply_to_status_id = temp_id, auto_populate_reply_metadata = True)
                print('invalid ticker')
        else:
            api.update_status('Invalid Command', in_reply_to_status_id = temp_id, auto_populate_reply_metadata = True)
            print('invalid command')
    else:
        print('no new tweets')
    time.sleep(30)