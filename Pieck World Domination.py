#PiECK WORLD DOMINATION
import tweepy 
import time

auth = tweepy.OAuthHandler('Gc8Zh4AtnnM4tnvw7YHj6ATwg','DpMgJcjW8QsF7Lbq0cvDsvEui1YNJWqwT4ylnacfzxUCcBRykD')
auth_set_access_token('1369256466146881538-FYNn935ybFCvJy6M8N692KBHnp8vE1','Jfd17r3sxy5iZXynM66FbtxEHW9uC3usOTi0K6IJPBaBK')


api = tweepy.API(auth, wait_on_rate_limit-True, wait_on_rate_limit_notify-True)


user = api.me()

print(user)

search = 'Pieck' 
ntwt = 100

for tweets in tweepy.Cursor(api.search, search).items(ntwt):
  try:
      print('Tweet favoritado e retuitado')
      tweet.retweet()
      tweet.favorite()
      time.sleep(43.200)
   except tweepy.TweepError as e:
      print(e.reason)
   except StopIteration:
      break
