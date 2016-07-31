# import redis
# import redisbayes
"""Teaches Redis how to properly associate text with a political candidate by teaching it candidate's tweets.
@author Shyam Thiagarajan
"""


"""Removes useless punctuation and formatting from tweet that would interfere in calculating word counts.
@param tweet
    tweet to format
@return formatted_tweet"""
def formatTweet(tweet):
    forbidden_characters = [',', '.', ':', '"', '(', ')']
    for forbidden_character in forbidden_characters:
        tweet = str(tweet.replace(forbidden_character, ''))
    if 'http' in tweet:
        tweet = tweet.split('http')[0]  # remove tweet content after url
    formatted_tweet = tweet.replace('\n', '').strip('\r').replace('  ', ' ').upper().lstrip().rstrip()
    return formatted_tweet


"""Stores tweets into @code companies
@param file_name
    file containing one column of tweets
        ex: We are experiencing an outage in Atlanta, GA.
            A tree fell over and knocked a power line out!
@returns tweets
    list of tweets"""
def readTweets(file_name):
    tweet_to_author = {}
    with open(file_name) as twitter_info:
        for tweet_info in twitter_info:
            tweet_info = eval(tweet_info.strip('\n'))  # Convert line (list literal) to list
            tweet = formatTweet(tweet_info[0])
            author = tweet_info[2]
            tweet_to_author[tweet] = author
    print tweet_to_author
    return tweet_to_author


"""Teaches Redis what a candidates said. Tweet and author is archived in redis (server)
@param tweets_to_candidates
    Dictionary of {tweet: candidate}"""
def teachAllCandidates(tweets_to_candidates):
    rb = redisbayes.RedisBayes(redis=redis.Redis())
    for tweet, author in tweets_to_candidates.items():
        rb.train(tweet, author)


"""Main Method That Teaches a brand new Redis
@updates Redis content
"""
def main():
    tweets_to_candidates = readTweets('../Twitter_Political_Analysis/candidate_tweets.txt')
    teachAllCandidates(tweets_to_candidates)


if __name__ == '__main__':
    main()