import tweepy
import wget

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def twitterHashtagImageExtract(hashtag):

    for tweet in tweepy.Cursor(api.search, q=hashtag, count=5,
                            lang="en").items():
        media_files = []
        media = tweet.entities.get('media', [])
        if len(media) > 0:
            print('GOT A PIC!')
            media_files.append(media[0]['media_url'])
        for media_file in media_files:
            wget.download(media_file)
        print(tweet.text)
