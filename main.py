import requests
import os
from instabot import Bot
from dotenv import load_dotenv
import re
import time
from pprint import pprint
import argparse


def get_users(text):
    return re.findall('(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)', text)


def is_user_exist(nickname):
    flag = False
    if bot.get_user_id_from_username(nickname):
        flag = True
    return flag


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Поиск победителей акции в instagram'
    )
    parser.add_argument('-l', '--login', help='Ваш логин в instagram')
    parser.add_argument('-p', '--password', help='Ваш пароль в instagram')
    parser.add_argument(
        '-a', '--author', help='Имя пользователя,автора поста-акции в instagram')
    parser.add_argument('-url', '--url_adress',
                        help='Адресс поста-акции в instagram')
    args = parser.parse_args()

    bot = Bot()
    bot.login(username=args.login, password=args.password)
    media_id = bot.get_media_id_from_link(args.url_adress)
    liker_list = bot.get_media_likers(media_id)

    followers_list = bot.get_user_followers(args.author)

    list_users = []
# для теста get_media_comments заменить на enumerate(bot.get_media_comments_all(media_id)) "https://www.instagram.com/p/BtON034lPhu/" 'beautybar.rus'
    
    for number, post in enumerate(bot.get_media_comments(media_id)):
        found_user = get_users(post['text'])
        existing_user = is_user_exist(''.join(get_users(post['text'])))
        username = bot.get_media_comments(media_id)[number]['user']['username']
        id_user = bot.get_user_id_from_username(username)

        if found_user and existing_user and (str(id_user) in liker_list) and (str(id_user) in followers_list):

            user = str(id_user), username
            list_users.append(user)
        print('Поиск победителей','.'*number,end='\r') 
        
        time.sleep(3)
    print()
    pprint(set(list_users))
