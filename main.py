#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-08 16:39
# Modified date : 2019-08-08 17:25
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from antiword import Antiword

def query():
    handler = Antiword()
    word = '批判'
    print(word)
    antiwords = handler.get_antiword(word)
    print("antiwords:")
    print(antiwords)

    print("simword:")
    simword = handler.get_simword(word)
    print(simword)

def run():
    query()

if __name__=="__main__":
    run()
