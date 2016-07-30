""" find word frequencies, word clouds, what words candidates end tweets with, remove punctuation later """


class TweetAnalysis:
    def __init__(self):
        self.twitter_data = []
        self.file_name = ''
        self.tweet_freq = {}


    """Sets the file path to read tweet data from.
    @param self
        TweetAnalysis object
    @param file_path
        path of data file
    @updates self.file_name"""
    def setFilePath(self, file_path):
        self.file_name = file_path


    """Stores contents in @code data_file and aggregates tweet information for all candidates.
    @param self
        Tweet Analysis Object
    @updates self.twitter_data
        Matrix representing aggregated tweet data
        Matrix = [[tweet, date, author, tweet location], ..., [tweet, date, author, tweet location]]
    """
    def create_tweet_lists(self):
        with open(self.file_name, 'r') as data_file:
            for tweet_info in data_file:
                tweet_info = eval(tweet_info.strip('\n'))   # Convert line (list literal) to list
                tweet_info[0] = self.formatTweet(tweet_info[0])
                print tweet_info
                self.twitter_data.append(tweet_info)


    """Removes useless punctuation from tweet that would interfere in comparing words
    @param self
        Tweet_Analysis object
    @param tweet
        tweet to format
    @return formatted_tweet"""
    def formatTweet(self, tweet):
        formatted_tweet = str(tweet.replace(',','').replace('.','').replace('\n','').strip('\r').replace('  ',' '))\
            .replace(':','').upper().lstrip().rstrip().replace('"','')
        if 'HTTP' in formatted_tweet:
            formatted_tweet = formatted_tweet.split('HTTP')[0]  # remove tweet content after url
        return formatted_tweet


    """Returns dictionary with keys representing candidate names and values representing number of
    respective tweets"""
    def getTweetFrequencies(self):
        for tweet_data in self.twitter_data:
            author = tweet_data[2]
            if author not in self.tweet_freq:
                self.tweet_freq[author] = 1
            else:
                self.tweet_freq[author] += 1
        return self.tweet_freq


    """Returns a JSON object with {candidate names: {word = wordcount}}"""
    def get_word_frequencies(self):
        self.word_frequencies = {}
        for index in range(len(self.twitter_data)):
            tweeter = self.twitter_data[index][2]
            tweet = self.twitter_data[index][0]
            if tweeter not in self.word_frequencies:
                self.word_frequencies[tweeter] = {}
            freq_list = self.individual_tweet_frequency(tweet)
            self.increment_frequency_dict(freq_list, tweeter)
        return self.word_frequencies

    """Returns dictionary of word frequencies for an individual Tweet_Analysis. """
    def individual_tweet_frequency(self, tweet):
        d = {}
        l = tweet.split(' ')
        for words in l:
            if 'https' not in words:
                if words not in d:
                    d[words] = 1
                else:
                    d[words] += 1
        return d

    """Appropriately increments word frequencies dictionary for words in the Tweet_Analysis"""
    def increment_frequency_dict(self, word_counts, tweeter):
        for words in word_counts:
            if words not in self.word_frequencies[tweeter]:
                self.word_frequencies[tweeter][words] = word_counts[words]
            else:
                self.word_frequencies[tweeter][words] += word_counts[words]


def main():
    test = TweetAnalysis()
    test.setFilePath('/home/dragon/Programs/TwitterApp/Twitter_Political_Analysis/candidate_tweets.txt')
    test.create_tweet_lists()
    print(test.getTweetFrequencies())
    candidates_word_maps = test.get_word_frequencies()
    print candidates_word_maps
    for keys, values in candidates_word_maps.items():
        print keys
        print values


if __name__ == '__main__':
    main()