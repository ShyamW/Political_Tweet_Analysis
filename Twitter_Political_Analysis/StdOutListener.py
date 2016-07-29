from tweepy.streaming import StreamListener
from Candidate_Tweet import CandidateTweet

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_status(self, status):
        print '!!!'
<<<<<<< HEAD
        print str(status)
        return True
=======
        tweet = CandidateTweet(status)
        tweet.outputTweets()
>>>>>>> 661f46686ead88173dccd3306c0624ee68094266


    def throwerror(self, status):
        print status