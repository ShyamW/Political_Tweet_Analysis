import tweepy
from Candidate_Tweet import Candidate_Tweet
import Log
import ConfigParser
from datetime import *
import sys

"""
@author
Shyam Thiagarajan

Python Program that fetches past tweets from a timeline of political candidates and records tweets and relevant metadata
(author and timestamp) for future analysis.
"""
class Past_Tweets():
    def __init__(self):
        self.candidate_tweets = []
        self.consumer_key = ''
        self.consumer_secret = ''
        self.key = ''
        self.secret = ''
        self.tweet_count = 0
        self.api = ''


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


    """Outputs Tweet_Analysis data to output file
    @updates output file content"""
    def outputTweets(self):
        out = open('Data/candidate_tweets.txt', 'a')
        for tweet in self.candidate_tweets:
            post = tweet.text
            date_time = tweet.date_time
            author = tweet.author
            location = tweet.source_loc
            output_data = [post, date_time, author, location]
            out.write(str(output_data) + '\n')
            print '!'
            print output_data
            print '!'
            print output_data


    """Gets tweets from timeline, gets metadata, and processes them.
    @requires
        successful login to Twitter
    """
    def findAndProcessTweets(self):
        global candidate_tweets
        self.candidate_tweets = []
        Log.record('\tWill Read From Config')
        self.readFromConfig()
        Log.record('\tWill Log into Twitter')
        self.loginToTwitter()
        Log.record('\tWill Fetch Tweets from Twitter')
        timeline = self.api.home_timeline(count=self.tweet_count)
        Log.record('\tSuccesfully Fetched Tweets from Twitter')
        for timeline_tweet in timeline:
            tweet = Candidate_Tweet(timeline_tweet)
            self.candidate_tweets.append(tweet)
            Log.record('\tPolitical Tweet Found!' + '\n\t' + '-'*30)
        self.outputTweets()



    """Fetches and records past tweets from political candidates"""
    def fetch(self):
        try:
            self.logEvents()
            self.findAndProcessTweets()
            Log.record('\tEverything Complete')
        except Exception as error:
            Log.record('SOMETHING WENT TERRIBLY WRONG!\n' + 'error: ' + str(error))


if __name__ == '__main__':
    twitter = Past_Tweets()
    twitter.fetch()


