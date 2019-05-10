import requests
import os
from instabot import Bot
import re
import time
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
    list_likers = bot.get_media_likers(media_id)

    list_followers = bot.get_user_followers(args.author)

    list_winners = []

    for post in bot.get_media_comments_all(media_id):
        candidate = post['user']['username']
        id_candidate = bot.get_user_id_from_username(candidate)

        print('Проверяем пользователя :', candidate,
              '                         ', end='\r')

        existing_user = []

        for user in set(get_users(post['text'])):
            existing_user.append(is_user_exist(user))

        if True in existing_user and (str(id_candidate) in list_followers) and (str(id_candidate) in list_likers):
            winner = str(id_candidate), candidate

            list_winners.append(winner)

        time.sleep(2)

    print()
    print('Список победителей :', set(list_winners))
