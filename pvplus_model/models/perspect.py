# coding: utf-8
from django.db import models

from pvplus_common.string_extension import get_uuid


class AppPerspectCommentGoods(models.Model):
    pk_key = models.CharField(primary_key=True, default=get_uuid(), max_length=40)
    pk_comment = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_perspect_comment_goods'


class AppPerspectComments(models.Model):
    pk_comment = models.CharField('id', primary_key=True,  default=get_uuid(),max_length=40)
    pk_perspect = models.CharField('决议id', max_length=40, blank=True, null=True)
    pk_user = models.CharField('用户id', max_length=40, blank=True, null=True)
    content = models.TextField('内容', max_length=300, blank=True, null=True)
    atuserid = models.CharField('@用户', max_length=40, blank=True, null=True)
    atcommentid = models.CharField('@评论', max_length=40, blank=True, null=True)
    floor = models.IntegerField('楼层', blank=True, null=True)
    goodnum = models.IntegerField('点赞数', default=0, blank=True, null=True)
    isaudited = models.NullBooleanField('是否审核', )
    createtime = models.DateTimeField('创建时间', auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_perspect_comments'
        verbose_name = u'决议评论'
        verbose_name_plural = u'决议评论列表'
        ordering = ['-createtime']

    def __str__(self):
        return self.content[:20]


class AppPerspectDowns(models.Model):
    pk_key = models.CharField(primary_key=True,  default=get_uuid(),max_length=40)
    pk_perspect = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_perspect_downs'
        ordering = ['-createtime']


class AppPerspectGoods(models.Model):
    pk_key = models.CharField(primary_key=True, default=get_uuid(), max_length=40)
    pk_perspect = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_perspect_goods'
        ordering = ['-createtime']


class AppPerspects(models.Model):
    pk_perspect = models.CharField('决议id', primary_key=True, default=get_uuid(), max_length=40)
    pk_stock = models.CharField('股票', max_length=40, blank=True, null=True)
    pk_user = models.CharField('用户id', max_length=40, blank=True, null=True)
    stockprice = models.DecimalField('股票价格', max_digits=18, decimal_places=2, blank=True, null=True)
    isbullish = models.NullBooleanField('是否看多', )
    expertprice = models.DecimalField('预期价格', max_digits=18, decimal_places=2, blank=True, null=True)
    expertrate = models.DecimalField('预期收益率', max_digits=18, decimal_places=2, blank=True, null=True)
    expertyearprofit = models.DecimalField('企业年利润', max_digits=18, decimal_places=2, blank=True, null=True)
    title = models.CharField('标题', max_length=200, blank=True, null=True)
    reason = models.TextField('原因', max_length=500, blank=True, null=True)
    commentnum = models.IntegerField('评论数', default=0, blank=True, null=True)
    goodnum = models.IntegerField('点赞数', default=0, blank=True, null=True)
    downnum = models.IntegerField('踩数', default=0, blank=True, null=True)
    isaudited = models.NullBooleanField('是否审核', )
    createtime = models.DateTimeField('创建时间', auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_perspects'
        verbose_name = '决议'
        verbose_name_plural = '决议列表'
        ordering = ['-createtime']

    def __str__(self):
        return self.title[:20]
