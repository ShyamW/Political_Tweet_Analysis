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


    """Reads tweet information from @code data_file and aggregates it for all candidates.
    @param self
        Tweet Analysis Object
    @updates self.twitter_data
        Matrix representing aggregated tweet data
        Matrix = [[tweet, date, author, tweet location], ..., [tweet, date, author, tweet location]]"""
    def createTweetLists(self):
        with open(self.file_name, 'r') as data_file:
            for tweet_info in data_file:
                tweet_info = eval(tweet_info.strip('\n'))   # Convert line (list literal) to list
                tweet_info[0] = self.formatTweet(tweet_info[0])
                print tweet_info
                self.twitter_data.append(tweet_info)


    """Removes useless punctuation and formatting from tweet that would interfere in calculating word counts.
    @param self
        Tweet_Analysis object
    @param tweet
        tweet to format
    @return formatted_tweet"""
    def formatTweet(self, tweet):
        forbidden_characters = [',', '.', ':', '"', '(', ')']
        for forbidden_character in forbidden_characters:
            tweet = str(tweet.replace(forbidden_character, ''))
        if 'http' in tweet:
            tweet = tweet.split('http')[0]  # remove tweet content after url
        formatted_tweet = tweet.replace('\n', '').strip('\r').replace('  ', ' ').upper().lstrip().rstrip()
        return formatted_tweet


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


    """Aggregates word frequencies from """
    def aggregateWordFreq(self, tweet_word_freq, author):
        for words in tweet_word_freq:
            if words not in self.word_frequencies[author]:
                self.word_frequencies[author][words] = tweet_word_freq[words]
            else:
                self.word_frequencies[author][words] += tweet_word_freq[words]


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
            tweet_word_freq = self.detTweetWordFreq(tweet)
            self.aggregateWordFreq(tweet_word_freq, author)


    """Gets the tweet word frequency dictionary.
        @param self
            Tweet Analysis object
        @return word frequency dictionary"""
    def getWordFrequencies(self):
        return self.word_frequencies


    """Returns dictionary of word frequencies for an individual Tweet"""
    def detTweetWordFreq(self, tweet):
        word_freq = {}
        all_words = tweet.split(' ')
        for word in all_words:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
        return word_freq



def main():
    test = TweetAnalysis()
    test.setFilePath('/home/dragon/Programs/TwitterApp/Twitter_Political_Analysis/candidate_tweets.txt')
    test.createTweetLists()
    test.detTweetFrequencies()
    print test.getTweetFrequencies()
    test.detWordFrequencies()
    candidates_word_maps = test.getWordFrequencies()
    for keys, values in candidates_word_maps.items():
        print keys
        print values


if __name__ == '__main__':
    main()