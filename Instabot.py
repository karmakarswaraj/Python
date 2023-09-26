from instabot import Bot 
bot = Bot()

bot.login(username = " ",password = " ")
#FOLLOW
bot.follow("username")

#UPLOAD
bot.upload_photo("path")

#UNFOLLOW
bot.unfollow("username")

#MESSAGE
bot.send_message("Hey, wassup?",["",""])

#COUNT FOLLOWING/FOLLOWERS
followers = bot.get_user_followers("username")
for i in followers:
    print(bot.get_user_followers(i))

