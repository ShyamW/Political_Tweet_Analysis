import Log
from datetime import *


"""This class represents all tweet and metadata (datetime, tweet content, author, and source_loc) in a standardized
way.

@author
    Shyam Thiagarajan
"""
class Candidate_Tweet():
    def __init__(self, timeline_tweet):
        self.date_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "-04")
        self.author = str(timeline_tweet.author.screen_name)
        try:
            self.text = str(timeline_tweet.text.encode('ascii', 'ignore').decode("utf-8").strip('\n').strip('\r'))
        except Exception:
            print 'Something Went Wrong'
            print Exception.__doc__
        try:
            self.source_loc = str(timeline_tweet.author.location.encode("utf-8").strip('\n'))
        except Exception:
            print 'Something Went Wrong'
            print Exception.__doc__
        Log.record("A Candidate's Tweet has been Found")
        Log.record(self.author)
        Log.record('\t' + self.date_time)



    """Outputs Tweet_Analysis data to output file
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

