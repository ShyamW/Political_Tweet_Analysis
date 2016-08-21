import tweepy
from tweepy import Stream
import Log
import ConfigParser
from datetime import *
from StdOutListener import StdOutListener

"""
@author
Shyam Thiagarajan

Python Program that streams tweets from a timeline of political candidates and records tweets and relevant metadata
(author and timestamp) for future analysis.
"""
class Streaming_Tweets():
    def __init__(self):
        self.consumer_key = ''
        self.consumer_secret = ''
        self.key = ''
        self.secret = ''


    """Reads parameters specified in config file. If no config file found, program will terminate.
    @updates twitter api keys
    """
    def readFromConfig(self):
        try:
            config = ConfigParser.ConfigParser()
            config.read('CONFIG.ini')
            self.consumer_key = (config.get('TwitterInfo', 'consumer_key'))
            self.consumer_secret = (config.get('TwitterInfo', 'consumer_secret'))
            self.key = (config.get('TwitterInfo', 'key'))
            self.secret = (config.get('TwitterInfo', 'secret'))
            self.tweet_count = int(config.get('TwitterInfo', 'tweet_count'))
            Log.record('\tSuccessfully read Config File')
        except:
            Log.record('INCORRECT Config, Application will now quit')
            sys.exit()


    """Logs in to Twitter using credentials.
    @updates self.api
        authenticated Tweepy object"""
    def loginToTwitter(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.key, self.secret)
        self.api = tweepy.API(auth)
        Log.record('\tSuccessfully Logged into Twitter')


    """Logs time and application divider in Log file"""
    def logEvents(self):
        Log.record('-' * 200)
        time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "-04")
        Log.record('\tApplication Ran at: ' + time)


    """Gets tweets from timeline, gets metadata, and processes them.
    @requires
        successful login to Twitter
    """
    def streamTwitter(self):
        Log.record('\tWill Read From Config')
        self.readFromConfig()
        Log.record('\tWill Log into Twitter')
        api = self.loginToTwitter()
        Log.record('\tWill Stream Tweets from Twitter')
        stream = Stream(self.api.auth, StdOutListener())
        stream.userstream('survey11909')


    """Main Method that streams and records live tweets """
    def stream(self):
        self.logEvents()
        self.streamTwitter()


if __name__ == '__main__':
    twitter = Streaming_Tweets()
    twitter.stream()


