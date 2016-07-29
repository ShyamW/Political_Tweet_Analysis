# find word frequencies, word clouds, what words candidates end tweets with, remove punctuation later
def __init___()
tweet_list = []
date_list = []
person_list = []
location_list = []
create_tweet_lists(filename)


"""Parses through Tweet_Analysis list and creates several lists corresponding to Tweet_Analysis attributes"""
def create_tweet_lists(self, filename):
    with open(filename, 'r') as f:
        for tweets in f:
            tweets = tweets.encode('ascii', 'ignore').decode("utf-8").strip('\n')
            print(str(tweets))
            tweet = eval(tweets)
            fixed_tweet = self.fixTweet(tweet[0])
            self.tweet_list.append(fixed_tweet)
            self.date_list.append(tweet[1])
            self.person_list.append(tweet[2])
            self.location_list.append(tweet[3])

"""Removes punctuation, URLS etc. from Tweet_Analysis"""
def fixTweet(self, tweet):
    return tweet.replace(',','').replace('.','')


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


"""Returns a 2D dictionary with keys = candidate names and values = dictionary consisting of their word counts"""
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




initial_filename = '/Users/jason/PycharmProjects/Projects/Tweet_Analysis/test.txt'
test = tweets(initial_filename)
print(test.getTweetFrequencies())
print(test.get_word_frequencies())