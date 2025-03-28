#!/bin/bash

query=$(rofi -dmenu -p "Яндекс")
[ -z "$query" ] && exit

xdg-open "https://yandex.ru/search/?text=${query// /+}"
