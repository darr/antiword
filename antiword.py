#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : antiword.py
# Create date : 2019-08-08 16:38
# Modified date : 2019-08-08 16:45
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import os

class Antiword:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        antifile = os.path.join(cur_dir, './data/antisem.txt')
        self.antidict, self.simdict = self.build_antidict(antifile)

    '''构造反义词词典'''
    def build_antidict(self, file):
        antidict = {}
        simdict = {}
        for line in open(file):
            line = line.strip().split(':')
            wd = line[0]
            antis = line[1].strip().split(';')
            if wd not in antidict:
                antidict[wd] = antis
            else:
                antidict[wd] += antis

            for anti in antis:
                if anti not in simdict:
                    simdict[anti] = [i for i in antis if i != anti]
                else:
                    simdict[anti] += [i for i in antis if i != anti]

        return antidict, simdict

    '''根据目标词获取反义词'''
    def get_antiword(self, word):
        return self.antidict.get(word, 'None')

    '''根据目标词获取近义词'''
    def get_simword(self, word):
        return self.simdict.get(word, 'no')

def demo():
    handler = Antiword()
    word = '批判'
    print(word)
    antiwords = handler.get_antiword(word)
    print(antiwords)
    for i in range(len(antiwords)):
        print(antiwords[i])


    simword = handler.get_simword(word)
    print(simword)
    for i in range(len(simword)):
        print(simword[i])

if __name__=="__main__":
    demo()
