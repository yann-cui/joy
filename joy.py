# -*- coding:utf-8 -*-

import sys

from rand import rand13to5, rand5to13
from game import run

def part_1():
    rand13to5()
    rand5to13()

def part_2():
    run()

def part_3():
    pass

if __name__ == "__main__":
    arg = sys.argv[1]
    
    if arg == 'part_1':
        part_1()
    elif arg == 'part_2':
        part_2()
    elif arg == 'part_3':
        part_3()
    else:
        pass