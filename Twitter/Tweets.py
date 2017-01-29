import tweepy

#
# Authentication
#
consumer_key = "GaRr5T6CGdxN5y9S4tykSDg0r"
consumer_secret = "HuAVktv85K4SKl9R0aZL8eqvBXe2gKOot9mpEt4lRx2dZ2SnYP"

#
# Access tokens
#
access_token = "182553513-B314r4nunmwWe3GcA4CNQ0w9rP1srApmNDPentX3"
access_token_secret = "2vBSc5JmqQr7loJTcvJJzGtdz4Vj6uSptdRy3CzzomGCH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweet_storage_file = 'tweets.txt'
my_latest_tweets = api.user_timeline(api.me().id, count=100, include_rts=False)

with open(tweet_storage_file, 'w', encoding='utf8') as f:
    for tweet in my_latest_tweets:
        f.write(tweet.text + '\n')





