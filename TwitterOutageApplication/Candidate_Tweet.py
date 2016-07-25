import Log


class CandidateTweet(object):
    def __init__(self, timeline_tweet):
        self.date_time = timeline_tweet.date_time
        Log.record('\t' + self.date_time)
        self.text = timeline_tweet.text
        self.twitter_id = timeline_tweet.author
        self.source_loc = timeline_tweet.auth_loc
        Log.record("A Candidate's Tweet has been Found")

