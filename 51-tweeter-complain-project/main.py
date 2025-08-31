from tweet import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10

# creating a new object
bot = InternetSpeedTwitterBot()

# navigating to speedtest.com

# getting the speed
bot.get_internet_speed()

# twitting..
bot.tweet_at_provider(PROMISED_DOWN, PROMISED_UP)





