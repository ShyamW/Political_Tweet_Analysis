import Log
from datetime import *

class CandidateTweet():

    def __init__(self, timeline_tweet):
        self.date_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "-04")
        Log.record('\t' + self.date_time)
        print "got data and time"
        try:
            self.text = str(timeline_tweet.text.encode('ascii', 'ignore').decode("utf-8").strip('\n').strip('\r'))
        except Exception:
            print 'SECOND TWEET ENCODING'
            print Exception.__doc__
            self.text = str(timeline_tweet.text.encode("utf-8").strip('\n'))
        self.author = str(timeline_tweet.author.screen_name)
        Log.record(self.author)
        try:
            self.source_loc = str(timeline_tweet.author.location.encode("utf-8").strip('\n'))
        except Exception:
            print 'SECOND TWEET ENCODING'
            self.auth_loc = str(timeline_tweet.author.location.encode('ascii', 'ignore').decode("utf-8").strip('\n'))
            print Exception.__doc__
        Log.record("A Candidate's Tweet has been Found")


    """Outputs tweet data to output file
    @param self
        Candidate_Tweet
    @updates output file content"""
    def outputTweets(self):
        out = open('candidate_tweets.txt', 'a')
        post = self.text
        date_time = self.date_time
        author = self.author
        location = self.source_loc
        output_data = [post, date_time, author, location]
        out.write(str(output_data) + '\n')

