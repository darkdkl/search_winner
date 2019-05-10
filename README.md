### Программа для поиска победителя конкурса в Instagram

#### Описание
Программа ищет победителя розыгрыша по выполненным условиям: 

<b>подписаться, поставить лайк и отметить друга</b>.

Используется библиотека instabot для доступа к API Instagram.

#### Установка

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей: 

```
pip3 install -r requirements.txt
```

#### Запуск программы:
для запуска программы необходимо передать следующие аргументы:
<b>-l </b> Ваш логин в instagram
<b>-p </b> Ваш пароль в instagram
<b>-a </b> Имя пользователя,автора поста-акции в instagram
<b>-url </b> Адрес поста-акции в instagram


Либо <b>-h </b>для справки :
```
usage: search_winner.py [-h] [-l LOGIN] [-p PASSWORD] [-a AUTHOR] [-url URL_ADRESS]

Поиск победителей акции в instagram

optional arguments:
  -h, --help            show this help message and exit
  -l LOGIN, --login LOGIN
                        Ваш логин в instagram
  -p PASSWORD, --password PASSWORD
                        Ваш пароль в instagram
  -a AUTHOR, --author AUTHOR
                        Имя пользователя,автора поста-акции в instagram
  -url URL_ADRESS, --url_adress URL_ADRESS
                        Адресс поста-акции в instagram


```
```
python3 search_winner.py -l you_login -p you_password -a post_author -u https://www.instagram.com/p/BtsNd3el22Pdu/
2019-05-10 19:59:05,908 - INFO - Instabot Started
2019-05-10 19:59:07,836 - INFO - Logged-in successfully as 'you_login'!
Getting followers of 1828755772: 100%|███████████████████████████████| 12753/12753 [00:20<00:00, 607.51it/s]
Проверяем пользователя : iron man    

Список победителей : {('6333612367', 'dsa.las018'), ('5534734339', 'random')}

```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.


##### Dark_Dmake
2019