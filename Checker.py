import os, time

class Checker():
    def __init__(self, artlasPath = "."):
        pass

    def check(self, fileName):
        return False, fileName

    def isLatest(self, fileName, modified):
        return int(os.path.getmtime(fileName)) == \
        int(time.mktime(time.strptime(str(modified), "%Y/%m/%d %H:%M:%S")))
        