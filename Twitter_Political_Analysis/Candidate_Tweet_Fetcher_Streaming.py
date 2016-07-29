import tweepy
from tweepy import Stream
import Log
import ConfigParser
from datetime import *
from StdOutListener import StdOutListener

"""
@author
Shyam Thiagarajan

Python Program that streams tweets from a timeline of political candidates.
"""
consumer_key = ''
consumer_secret = ''
key = ''
secret = ''
tweet_count = 0


"""Reads parameters specified in config file. If no config file found, will use default values
@updates global defaults
"""
def readFromConfig():
    global consumer_key
    global consumer_secret
    global key
    global secret
    try:
        config = ConfigParser.ConfigParser()
        config.read('CONFIG.ini')
        consumer_key = (config.get('TwitterInfo', 'consumer_key'))
        consumer_secret = (config.get('TwitterInfo', 'consumer_secret'))
        key = (config.get('TwitterInfo', 'key'))
        secret = (config.get('TwitterInfo', 'secret'))
        Log.record('\tSuccessfully read Config File')
    except:
        Log.record('INCORRECT Config, REVERTING BACK TO DEFAULTS')


"""Logs in to Twitter using credentials.
@return api
    authenticated Tweepy object"""
def loginToTwitter():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth)
    Log.record('\tSuccessfully Logged into Twitter')
    return api


"""Logs time and application divider in Log file"""
def logEvents():
    Log.record('-' * 200)
    time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "-04")
    Log.record('\tApplication Ran at: ' + time)


"""Gets tweets from timeline, gets metadata, and processes them.
@requires
    successful login to Twitter
"""
def streamTwitter():
    Log.record('\tWill Read From Config')
    readFromConfig()
    Log.record('\tWill Log into Twitter')
    api = loginToTwitter()
    Log.record('\tWill Stream Tweets from Twitter')
    stream = Stream(api.auth, StdOutListener())
    stream.userstream('survey11909')


"""Main Method that updates outage information to a database. Processes 15 tweets"""
def main():
    logEvents()
    streamTwitter()


if __name__ == '__main__':
    main()


