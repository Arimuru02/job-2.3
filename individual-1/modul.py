# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

def fun1(to_replace, replacer):

    def fun(string):
        nonlocal to_replace, replacer
        result = string.replace(replacer, to_replace)
        return result

    return fun
