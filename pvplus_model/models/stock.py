# coding: utf-8
from django.db import models


class AppStock(models.Model):
    pk_stock = models.CharField('股票代码', primary_key=True, max_length=40)
    stockname = models.CharField('股票名称', max_length=100, blank=True, null=True)
    tradetype = models.CharField('股票类型', max_length=100, blank=True, null=True)
    isdisabled = models.NullBooleanField('是否启用', )
    istop = models.NullBooleanField('是否置顶', )
    sortno = models.IntegerField('排序号', blank=True, null=True)
    createtime = models.DateTimeField('创建时间', auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_stock'
        verbose_name = '股票'
        verbose_name_plural = '股票列表'

    def __str__(self):
        return self.pk_stock + ':' + self.stockname
