""" find word frequencies, word clouds, what words candidates end tweets with, remove punctuation later """

class TweetAnalysis:
    def __init__(self):
        self.twitter_data = []
        self.file_name = ''
        self.tweet_freq = {}
        self.word_frequencies = {}


    """Sets the file path to read tweet data from.
    @param self
        TweetAnalysis object
    @param file_path
        path of data file
    @updates self.file_name"""
    def setFilePath(self, file_path):
        self.file_name = file_path


    """Removes useless punctuation and formatting from tweet that would interfere in calculating word counts.
        @param self
            Tweet_Analysis object
        @param tweet
            tweet to format
        @return formatted_tweet"""
    def formatTweet(self, tweet):
        forbidden_characters = [',', '.', ':', '"', '(', ')', '!', '-', '&amp;', ';', '']
        for forbidden_character in forbidden_characters:
            tweet = str(tweet.replace(forbidden_character, ''))
        unimportant_words = [' and ', ' the ', ' to ', ' a ', ' do ', ' be ', ' on ', ' is ', ' in ', ' of ']
        for unimportant_word in unimportant_words:
            tweet = str(tweet.replace(unimportant_word, ' '))
        if 'http' in tweet:
            tweet = tweet.split('http')[0]  # remove tweet content after url
        formatted_tweet = tweet.replace('\n', '').strip('\r').replace('  ', ' ').upper().lstrip().rstrip()
        return formatted_tweet


    """Reads tweet information from @code data_file and aggregates it for all candidates.
    @param self
        Tweet Analysis Object
    @updates self.twitter_data
        Matrix representing aggregated tweet data
        Matrix = [[tweet, date, author, tweet location], ..., [tweet, date, author, tweet location]]"""
    def createTweetLists(self):
        with open(self.file_name, 'r') as tweets_file:
            for tweet_info in tweets_file:
                tweet_info = eval(tweet_info.strip('\n'))   # Convert line (list literal) to list
                tweet_info[0] = self.formatTweet(tweet_info[0])
                print tweet_info
                self.twitter_data.append(tweet_info)


    """Determines tweet frequencies for each candidate.
    @param self
        Tweet Analysis object
    @updates
        self.tweet_freq
    @ensures
        if author not in tweet_freq dictionary:
            author is added as key
            value = 1
        else:
            author's value (tweet frequency) is incremented
    """
    def detTweetFrequencies(self):
        for tweet_data in self.twitter_data:
            author = tweet_data[2]
            if author not in self.tweet_freq:
                self.tweet_freq[author] = 1
            else:
                self.tweet_freq[author] += 1


    """Gets the tweet Frequency dictionary.
    @param self
        Tweet Analysis object
    @return self.tweet_freq"""
    def getTweetFrequencies(self):
        return self.tweet_freq


    """Creates a JSON object with {candidate names: {word = wordcount}}.
    @param self
        Tweet Analysis Object
    @updates self.word_frequencies"""
    def detWordFrequencies(self):
        for tweet_info in self.twitter_data:
            author = tweet_info[2]
            if author not in self.word_frequencies:
                self.word_frequencies[author] = {}
            tweet = tweet_info[0]
            self.detTweetWordFreq(tweet, author)


    """Gets the tweet word frequency dictionary.
    @param self
        Tweet Analysis object
    @return word frequency dictionary"""
    def getWordFrequencies(self):
        return self.word_frequencies


    """Returns dictionary of word frequencies for an individual Tweet
    @param self
        Tweet Analysis object
    @param tweet
        Tweet to analyze
    @param author
        name of candidate"""
    def detTweetWordFreq(self, tweet, author):
        word_frequencies = self.word_frequencies[author]
        all_words = tweet.split(' ')
        for word in all_words:
                if word in word_frequencies:
                    word_frequencies[word] += 1
                else:
                    word_frequencies[word] = 1