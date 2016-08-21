# Documentation

This Python project fetches and streams political tweets and analyzes each politician's tweets through graphs and wordmaps.

#### Analyzed rhetoric elements include:
 * diction (word choice and frequency)
 * syllables
 * tweet time
 * tweet frequency

#### This Project fetches tweets from several famous political candidates including:
* Donald Trump (@realDonaldTrump)
* Hillary Clinton (@HillaryClinton)
* Jeb Bush (@JebBush)
* John Kasich (@JohnKassich)
* Ted Cruz (@tedcruz)
* Carly Fiorina (@CarlyFiorina)
* Bernie Sanders (@BernieSanders)
* Marco Rubio (@marorubio)
* President Obama (@POTUS and @BarrackObama)


#### Basic Requirements:
1. [Python 2.X (Required)](https://www.python.org/downloads/)
	* Python 2.7 recommended

			sudo apt-get install python

2. [ConfigParser (Required)](https://pypi.python.org/pypi/configparser)
	* Used to Read API Key information

        	pip install ConfigParser

3. [datetime (Required)](https://pypi.python.org/pypi/DateTime)
	* Used to Get Python Standardized time (included in python 2.7)

        	pip install datetime

#### Requirements to Fetch and Stream Tweets
1. [tweepy (Optional)](http://docs.tweepy.org/en/v3.5.0/install.html)
    * Used to stream and fetch tweets. Unnecessary for Analyzing tweets.

            pip install tweepy

#### Requirements to Analyze Tweets
1. [matplotlib (Optional)](http://matplotlib.org/downloads.html)
    * Used to create graphs

            pip install matplotlib

2. [TkInter (Optional)](https://wiki.python.org/moin/TkInter)
    * Used in graph creation

            sudo apt-get install python python-tk


