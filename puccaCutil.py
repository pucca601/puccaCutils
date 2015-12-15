me: puccaCutil.py
# Description: pucca's custom tool utility
# Usage: null
# Author: pucca601
# Date: 2015.12.15
# moreinfo: null

import time
import os
import sys
import json
import shutil
import ConfigParser
import subprocess

class Cutil(object):
    
    @staticmethod
    def isRemoveEmptyDirs(fileDir):
        if os.path.isfile(fileDir):
            extName = os.path.split(fileDir)[1]
            if extName == ".DS_Store":
                return True
            else:
                return False
        elif os.path.isdir(fileDir):
            isRemove = True
            for subFileDir in os.listdir(fileDir):
                subFileDir = os.path.join(fileDir, subFileDir)
                if Cutil.isRemoveEmptyDirs(subFileDir):
                    try:
                        os.rmdir(subFileDir)
                        print('remove success')
                    except Exception as e:
                        pass
                else:
                    isRemove = False
            return isRemove
        else:
            return False

