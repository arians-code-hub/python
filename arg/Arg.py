import sys

sys.path.append('./..')

from util.variable import Convert

class Arg:
    @staticmethod
    def actualArgs(actual=True):
        return sys.argv[1:] if actual else sys.argv

    @staticmethod
    def parseKeyVal(arg):
        index = -1
        for i in range(len(arg)):
            if arg[i] == ':':
                index = i
                break
        return None if index == -1 else (arg[:index], arg[index + 1:])

    @staticmethod
    def keyValue(actual=True, tryConverting=True,defaults={}):
        # key:value
        # "key:value"
        dic = {}
        for arg in Arg.actualArgs(actual):
            tmp = Arg.parseKeyVal(arg)
            if tmp is None:
                sec = Convert.toNumber(tmp) if tryConverting else tmp
                sec = tmp if sec is None else sec
            else:
                sec = Convert.toNumber(tmp[1]) if tryConverting else tmp[1]
                sec = tmp[1] if sec is None else sec
            dic[tmp[0]] = sec
        for key in defaults:
            if key not in dic:
                dic[key] = defaults[key]
        return dic
