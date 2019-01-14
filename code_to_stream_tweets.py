#twitter, json and csv must be imported to run the code
import twitter,json,csv

#consumer keys are taken from the twitter developed account
#these must be inputted so the code can access twiter through your account
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = 'F'
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# the tweets will be collected in this csv file
csvfile = open('israel_12Dec.csv', 'w')
csvwriter = csv.writer(csvfile, delimiter='|')

#  a function that removes breakable characters, and makes sure that all the characters in different languages can be read through utf-8.
def getVal(val):
    clean = ""
    if val:
        val = val.replace('|', ' ')
        val = val.replace('\n', ' ')
        val = val.replace('\r', ' ')
        clean = val.encode('utf-8')
    return clean


q = "searchterm" # Can add a list of terms, separated by a comma
print 'Filtering the public timeline for track="%s"' % (q,)

twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

stream = twitter_stream.statuses.filter(track=q)

#this is the list of attributes that will be collected from the stream and imported into the scv as columns, making analysis much easier
for tweet in stream:
    csvwriter.writerow([
        tweet['created_at'],
        getVal(tweet['user']['screen_name']),
        # getVal(tweet_text),
        getVal(tweet['text']),
        getVal(tweet['user']['location']),
        tweet['user']['statuses_count'],
        tweet['user']['followers_count'],
        tweet['user']['friends_count'],
        tweet['user']['created_at'],
        tweet['id']
        ])
    # This prints the stream on the screen in real time. Really cool to look at, but not much use other than saying that the code is working (or not)
    print tweet['user']['screen_name'].encode('utf-8'), tweet['text'].encode('utf-8')
