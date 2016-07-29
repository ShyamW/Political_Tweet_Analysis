from tweepy.streaming import StreamListener
from Candidate_Tweet import CandidateTweet

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream."""
    def on_status(self, status):
        try:
            print '!!!'
            tweet = CandidateTweet(status)
            tweet.outputTweets()
        except:
            print 'Something went wrong, Continuing to stream'


    def throwerror(self, status):
        print status