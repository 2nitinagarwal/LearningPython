import json
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

consumer_key = 'u8PlyCqzlI5S1rTLzV4MyeSRj'
consumer_secret = 'uACqANk1YkTXG6WVfJUD3OGekHzyRWpVn8ci7nSXgZiaMk1cNe'
access_token = '80389170-uNoogWZxSIgePfrBkuD3c7KFNjRmhUR8ZIraD8JaF'
access_token_secret = 'omRzxq0AwGGm09aeqEDC0NtTQ5Vp45Mna1eAbJDLzPwSM'

auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

class PrintListener(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':
            print(status.text.encode("utf-8"))
            print(status.author.screen_name.encode("utf-8"), status.created_at, status.source.encode("utf-8"), '\n')

    def on_error(self, status_code):
        print("Error code: {}".format(status_code))
        return True # keep stream live

    def on_timeout(self):
        print('Listener timed out!')
        return True # keep stream alive

def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ( 'en',)
    stream.sample(languages=languages)

def pull_down_tweets(screen_name):
    api = API(auth)
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    for tweet in tweets:
        print(json.dumps(tweet._json, indent=4))


if __name__ == '__main__':
    # print_to_terminal()
    pull_down_tweets('IAmNitinAgarwal')
