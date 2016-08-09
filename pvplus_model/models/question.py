# coding: utf-8
from django.db import models

from pvplus_common.string_extension import get_uuid

QUESTION_MODE = (
    ('free', '免费提问'),
    ('push', '付费提问'),
    ('onetoone', '一对一提问')
)


class AppQuestions(models.Model):
    pk_question = models.CharField('问答id', primary_key=True, max_length=40,default=get_uuid())
    pk_user = models.CharField('用户id', max_length=40, blank=True, null=True)
    content = models.CharField('提问内容', max_length=2000, blank=True, null=True)
    questionmode = models.CharField('提问方式', choices=QUESTION_MODE, max_length=20, blank=True, null=True)
    questionrelate = models.CharField('提问相关', max_length=20, blank=True, null=True)
    pk_respondent = models.CharField('回复者id', max_length=40, blank=True, null=True)
    listennum = models.IntegerField('偷听人数', default=0, blank=True, null=True)
    isopen = models.NullBooleanField('是否公开', null=True)
    iscommented = models.NullBooleanField('是否已评论', null=True)
    question_price = models.DecimalField('提问价格', max_digits=18, decimal_places=4, blank=True, null=True)
    listen_price = models.DecimalField('偷听价格', max_digits=18, decimal_places=4, blank=True, null=True)
    goodnum = models.IntegerField('点赞数', default=0, blank=True, null=True)
    commentnum = models.IntegerField('评论数', default=0, blank=True, null=True)
    status = models.IntegerField('状态', blank=True, null=True)
    createtime = models.DateTimeField('创建时间', auto_now_add=True, blank=True, null=True)
    updatetime = models.DateTimeField('用户id', auto_now=True, blank=True, null=True)
    isaudited = models.NullBooleanField('是否审核', null=True)

    class Meta:
        managed = False
        db_table = 'app_questions'
        verbose_name = '提问'
        verbose_name_plural = '提问列表'
        ordering = ['-createtime']

    def __str__(self):
        return self.content[:20]


class AppQuestionComments(models.Model):
    pk_comment = models.CharField(primary_key=True, default=get_uuid(), max_length=40)
    pk_question = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    rating = models.IntegerField(blank=True, default=0, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    isaudited = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'app_question_comments'
        ordering = ['-createtime']


class AppQuestionGoods(models.Model):
    pk_key = models.CharField(primary_key=True, default=get_uuid(), max_length=40)
    pk_question = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_question_goods'
        ordering = ['-createtime']


class AppAnswers(models.Model):
    pk_answer = models.CharField('回答id', primary_key=True, default=get_uuid(), max_length=40)
    pk_question = models.CharField('提问id', max_length=40, blank=True, null=True)
    pk_user = models.CharField('用户id', max_length=40, blank=True, null=True)
    voice = models.CharField('音频路径', max_length=200, blank=True, null=True)
    duration = models.IntegerField('时长', blank=True, null=True)
    content = models.TextField('文本内容', max_length=1000, blank=True, null=True)
    isbest = models.NullBooleanField('是否最佳', )
    createtime = models.DateTimeField('创建时间', auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_answers'
        verbose_name = '回答'
        verbose_name_plural = '回答列表'
        ordering = ['-createtime']


class AppListens(models.Model):
    pk_listen = models.CharField('id', primary_key=True,  default=get_uuid(),max_length=40)
    pk_question = models.CharField('提问id', max_length=40, blank=True, null=True)
    pk_user = models.CharField('用户', max_length=40, blank=True, null=True)
    iscommented = models.NullBooleanField('是否已评论', )
    createtime = models.DateTimeField('创建时间', auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_listens'
        verbose_name = '偷听'
        verbose_name_plural = '偷听列表'
        ordering=['-createtime']

    def __str__(self):
        return self.pk_listen
