import tweepy
from Candidate_Tweet import CandidateTweet
import Log
import ConfigParser
from datetime import *

"""
@author
Shyam Thiagarajan

Python Program that fetches tweets from a timeline of political candidates.
"""
candidate_tweets = []
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
    global tweet_count
    try:
        config = ConfigParser.ConfigParser()
        config.read('CONFIG.ini')
        consumer_key = (config.get('TwitterInfo', 'consumer_key'))
        consumer_secret = (config.get('TwitterInfo', 'consumer_secret'))
        key = (config.get('TwitterInfo', 'key'))
        secret = (config.get('TwitterInfo', 'secret'))
        tweet_count = int(config.get('TwitterInfo', 'tweet_count'))
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


"""Outputs tweet data to output file
@param candidate_tweets
    list of candidate's tweets
@updates output file content"""
def outputTweets(candidate_tweets):
    out = open('candidate_tweets.txt', 'a')
    for tweet in candidate_tweets:
        post = tweet.text
        date_time = tweet.date_time
        author = tweet.author
        location = tweet.auth_loc
        output_data = [post, date_time, author, location]
        out.write(str(output_data) + '\n')



"""Gets tweets from timeline, gets metadata, and processes them.
@requires
    successful login to Twitter
"""
def findAndProcessTweets():
    global candidate_tweets
    candidate_tweets = []
    Log.record('\tWill Read From Config')
    readFromConfig()
    Log.record('\tWill Log into Twitter')
    api = loginToTwitter()
    Log.record('\tWill Fetch Tweets from Twitter')
    timeline = api.home_timeline(count=tweet_count)
    Log.record('\tSuccesfully Fetched Tweets from Twitter')
    for timeline_tweet in timeline:
        tweet = CandidateTweet(timeline_tweet)
        candidate_tweets.append(tweet)
        Log.record('\tPolitical Tweet Found!' + '\n\t' + '-'*30)
    outputTweets(candidate_tweets)



"""Main Method that updates outage information to a database. Processes 15 tweets"""
def main():
    try:
        logEvents()
        findAndProcessTweets()
        Log.record('\tEverything Complete')
    except Exception as error:
        Log.record('SOMETHING WENT TERRIBLY WRONG!\n' + 'error: ' + str(error))

if __name__ == '__main__':
    main()


