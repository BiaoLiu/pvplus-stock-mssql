# coding: utf-8
from django.db import models

from pvplus_common.string_extension import get_uuid


class AppMsg(models.Model):
    pk_msg = models.CharField(primary_key=True, default=get_uuid(), max_length=40)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    pk_receive = models.CharField(max_length=40, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    msgtype = models.CharField(max_length=20, blank=True, null=True)
    isaudit = models.NullBooleanField()
    createtime = models.DateTimeField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_msg'


class AppMsgRecord(models.Model):
    pk_record = models.CharField(primary_key=True, default=get_uuid(), max_length=40)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    pk_relate = models.CharField(max_length=40, blank=True, null=True)
    msgtype = models.CharField(max_length=20, blank=True, null=True)
    isread = models.NullBooleanField()
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_msg_record'