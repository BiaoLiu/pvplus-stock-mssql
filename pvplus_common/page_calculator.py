# coding:utf-8

class PageCalculator():
    @staticmethod
    def start(pindex, psize):
        return (pindex - 1) * psize

    @staticmethod
    def end(pindex, psize):
        return pindex * psize
