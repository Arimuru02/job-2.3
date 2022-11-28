# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import sys
from modul import fun1

if __name__ == "__main__":
    x = input("Введите строку: ")
    c = input("Введите символ, который нужно заменить: ")
    h = input("Введите символ, на который заменить: ")
    rep = fun1(h, c)
    print(rep(x))