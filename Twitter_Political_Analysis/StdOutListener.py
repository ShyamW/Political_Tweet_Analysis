from tweepy.streaming import StreamListener
from Candidate_Tweet import CandidateTweet

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    print 'Looking for tweets...'

    def on_status(self, status):
        print '!!!'
        Tweet = CandidateTweet(status)
        return True

    def throwerror(self, status):
        print status