import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools


#first getting tweets with keyword=MassekaGamestud, unfortunately nothing shows up for masseka golden georges

loc = '43.6042600, 1.4436700, 10km'
keyword = "MassekaGamestud"

#scrapping 5 tweets and stores them as dataframe, just a sample
df_coord = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
    keyword.format(loc)).get_items(), 5))[['user', 'date','content']]

# create a new column for user_location
df_coord['user_location'] =  df_coord['user'].apply(lambda x: x['location'])

#df got datetime64[ns, UTC]
df_coord['date'] = df['date'].dt.tz_localize(None)

print(df_coord)

df_coord.to_json(r"C:\Users\21266\Desktop\ydays_project\output.json")

































#-------------------------------------NEEDS ELEVATED PRIVILEGES------------------------------
import tweepy 
#CREATING API CONNEXION
#ADDING KEYS
CONSUMER_KEY = 'meecz7cqWmK0xBmzKWoUMcgij'
CONSUMER_SECRET = 'yMsIajYBcALG1ieV0SbtP11yi6rqbgeDOrYDsaK2i5mEXsoQsV'
OAUTH_TOKEN = '1460991855202648064-7ypJqupqjIGyadl2Y8OvH3Ngxrimyy'
OAUTH_TOKEN_SECRET = 'Bu4VDBWgqqy9MqLTw2JewdVsJYzm0dVMTly5zq8NXsq14'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  
# setting access to user's access key and access secret 
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
  
# calling the api 
twitter_api = tweepy.API(auth)

id = 57741058
 
# fetching the user
user = twitter_api.get_user(id)
 
# fetching the location
location = user.location
 
print("The location of the user is : " + location)

#---------------------------------------------------------------------------------------------------
