#!/usr/bin/env python3
from os import system

url = input("url? ")

system('open "https://twitter.com/intent/tweet?text=@adm1nkyj1%20start_analysis(%22{url}%22);"'.format(url=url))
