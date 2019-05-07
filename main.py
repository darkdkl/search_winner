import requests
import os
from instabot import Bot
from dotenv import load_dotenv

bot = Bot()
bot.login(username=os.getenv('LOGIN'), password=os.getenv('PASSWORD'))
media_id=bot.get_media_id_from_link("https://www.instagram.com/p/Bqe7BOsjIGA/")
for number,post in enumerate(bot.get_media_comments_all(media_id)):
    print(post['text'],)
    