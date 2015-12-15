#!/usr/bin/env python
# coding=utf-8
# Author: pucca601

import sys, os
from puccaCutil import Cutil

def main(argv=sys.argv):
    print(argv[1:])
    if len(argv) < 2:
        print('parameter error')
        sys.exit(-1)
    dir_path = argv[1]
    file_types = argv[2:]
    isRemoveEmptyDirs = Cutil.isRemoveEmptyDirs(dir_path)
    print(isRemoveEmptyDirs)

if __name__ == '__main__':
    main()
