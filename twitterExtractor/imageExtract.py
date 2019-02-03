import tweepy
import wget

consumer_key = "vFPG1asGLNNM3qV8pWoYptJTl"
consumer_secret = "ed68y4Gyf5gS1AZQg4RoU3N44uxTzajFAIyzUT2G0OM0ZHj4VU"
access_token = "2965059837-0jVHykIe1NWJPbW1K8SwEMdQJHgSsnEomH0wyjl"
access_token_secret = "MqXbn4IU6fafRZgeqgLetFxeiP3AzyPhYzRlPPINLwiST"

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
