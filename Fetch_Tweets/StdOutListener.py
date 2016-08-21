from tweepy.streaming import StreamListener
from Candidate_Tweet import Candidate_Tweet

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream."""
    def on_status(self, status):
        try:
            print '!!!'
            tweet = Candidate_Tweet(status)
            tweet.outputTweets()
        except:
            print 'Something went wrong, Continuing to stream'


    def throwerror(self, status):
        print status