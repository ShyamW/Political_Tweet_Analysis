from tweepy.streaming import StreamListener
from Candidate_Tweet import CandidateTweet

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, status):
        print '!!!'
        tweet = CandidateTweet(status)
        tweet.outputTweets()
        return True

    def on_error(self, status):
        print status