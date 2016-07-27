import Log
from datetime import *

class CandidateTweet(object):
    def __init__(self, timeline_tweet):
        self.date_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "-04")
        Log.record('\t' + self.date_time)
        try:
            self.text = str(timeline_tweet.text.encode("utf-8").strip('\n').decode("utf-8"))
        except:
            self.text = str(timeline_tweet.text.encode("utf-8").strip('\n'))
        self.author = str(timeline_tweet.author.screen_name)
        Log.record(self.author)
        self.source_loc = str(timeline_tweet.author.location.encode("utf-8").strip('\n'))
        Log.record("A Candidate's Tweet has been Found")

