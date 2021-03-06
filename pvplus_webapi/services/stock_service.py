# coding:utf-8
import urllib

from django.db.models import Q

from pvplus_common.page_calculator import PageCalculator
from pvplus_model.models.stock import AppStock

stock_url = 'http://qt.gtimg.cn/q={}'


class StockService():
    def get_stocks(self, keyword, sorttype, sortno, pindex, psize):
        stocks = AppStock.objects.filter(isdisabled=True)

        psize = psize if psize <= 30 else 30
        # 关键字搜索
        if not keyword:
            stocks = stocks.filter(Q(stockname__contains=keyword) | Q(pk_stock__contains=keyword))

        stock_dtos = []
        stocks = list(stocks)
        for item in stocks:
            stock = self.get_response(item.stockname, item.pk_stock, item.tradetype)
            stock_dtos.append(stock)

        stock_dtos = stock_dtos[PageCalculator.start(pindex, psize): PageCalculator.end(pindex, psize)]

        reverse = sortno == 'desc'
        sort = ['lastprice', 'changeamount', 'changerate']
        # 排序
        sorttype = sorttype if sorttype in sort else 'lastprice'

        stock_dtos = sorted(stock_dtos, key=lambda s: s[sorttype], reverse=reverse)
        # stock_dtos = stock_dtos.sort(key=key, reverse=reverse)

        return stock_dtos

    def get_response(self, stockname, stockcode, tradetype):
        response = urllib.request.urlopen(stock_url.format(tradetype + stockcode))
        # result=bytes.decode(response.read())
        result = response.read().decode('gbk')

        stockinfo = result.split('~')
        stock_dto = {}

        stock_dto['stockname'] = stockname
        stock_dto['stockcode'] = stockcode
        stock_dto['lastprice'] = convert_to_float(stockinfo[3])
        stock_dto['prevclose'] = convert_to_float(stockinfo[4])
        stock_dto['open'] = convert_to_float(stockinfo[5])
        stock_dto['changeamount'] = convert_to_float(stockinfo[31])
        stock_dto['changerate'] = convert_to_float(stockinfo[32])
        stock_dto['highest'] = convert_to_float(stockinfo[33])
        stock_dto['lowest'] = convert_to_float(stockinfo[34])
        stock_dto['tradingvolume'] = convert_to_float(stockinfo[36])
        stock_dto['changingover'] = convert_to_float(stockinfo[37])
        stock_dto['turnoverrate'] = convert_to_float(stockinfo[38])
        stock_dto['peratio'] = convert_to_float(stockinfo[39])
        stock_dto['circulatecap'] = convert_to_float(stockinfo[44])
        stock_dto['totalcap'] = convert_to_float(stockinfo[45])
        stock_dto['pbratio'] = convert_to_float(stockinfo[46])

        return stock_dto


def convert_to_float(source):
    return float(source) if source else 0
