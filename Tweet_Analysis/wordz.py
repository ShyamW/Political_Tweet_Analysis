""" find word frequencies, word clouds, what words candidates end tweets with, remove punctuation later """


class TweetAnalysis:
    def __init__(self):
        self.tweet_list = []
        self.date_list = []
        self.person_list = []
        self.location_list = []
        self.file_name = ''


    """Sets the file path to read tweet data from.
    @param self
        TweetAnalysis object
    @param file_path
        path of data file
    @updates self.file_name"""
    def setFilePath(self, file_path):
        self.file_name = file_path


    """Parses through @code data_file and creates several lists corresponding to Tweet_Analysis attributes
    @param self
        Tweet Analysis Object"""
    def create_tweet_lists(self):
        with open(self.file_name, 'r') as data_file:
            for tweet_info in data_file:
                tweet_info = tweet_info.strip('\n')
                tweet_info = eval(tweet_info)
                print 'AAA'
                print tweet_info
                print 'AAA'
                fixed_tweet = self.fixTweet(tweet_info[0])
                self.tweet_list.append(fixed_tweet)
                self.date_list.append(tweet_info[1])
                self.person_list.append(tweet_info[2])
                self.location_list.append(tweet_info[3])

    """Removes punctuation, URLS etc. from Tweet_Analysis"""
    def fixTweet(self, tweet):
        fixed_tweet = tweet.replace(',','').replace('.','').strip('\n').strip('\r').replace('  ',' ').decode('utf-8')
        print fixed_tweet
        return fixed_tweet


    """Returns dictionary with keys representing candidate names and values representing number of
    respective tweets"""
    def getTweetFrequencies(self):
        self.tweet_freq = {}
        for names in self.person_list:
            if names not in self.tweet_freq:
                self.tweet_freq[names] = 1
            else:
                self.tweet_freq[names] += 1
        return self.tweet_freq


    """Returns a JSON object with {candidate names: {word = wordcount}}"""
    def get_word_frequencies(self):
        self.word_frequencies = {}
        for index in range(len(self.tweet_list)):
            tweeter = self.person_list[index]
            tweet = self.tweet_list[index]
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