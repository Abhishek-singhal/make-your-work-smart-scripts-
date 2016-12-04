import tweepy

consumer_key = "xyz"
consumer_secret = "Abc"

access_token = "xyz"
access_token_secret = "xyz"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#print api.home_timeline()
print("Enter the handle name of person whom u want to see tweets")
abc=input()
public_tweets = api.user_timeline(id=str(abc),count='200')

i=1
for tweet in public_tweets:        
    print(str(i)+" "+tweet.text)
    i=i+1
    



