# coding: utf-8
from django.db import models

from pvplus_common.string_extension import get_uuid


class AppUserAttentions(models.Model):
    pk_attention = models.CharField(primary_key=True, default=get_uuid(), max_length=40)
    attentionid = models.CharField(max_length=40, blank=True, null=True)
    relateobj = models.CharField(max_length=20, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_user_attentions'


class AppUserAttr(models.Model):
    pk_user = models.CharField(primary_key=True, max_length=40)
    stock_attentionnum = models.IntegerField(blank=True, null=True)
    perspect_attentionnum = models.IntegerField(blank=True, null=True)
    user_attentionnum = models.IntegerField(blank=True, null=True)
    followernum = models.IntegerField(blank=True, null=True)
    perspectnum = models.IntegerField(blank=True, null=True)
    questionnum = models.IntegerField(blank=True, null=True)
    answernum = models.IntegerField(blank=True, null=True)
    rewardnum = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_user_attr'


class AppUserProfile(models.Model):
    pk_user = models.CharField(primary_key=True, max_length=40)
    realname = models.CharField(max_length=100, blank=True, null=True)
    isverified = models.NullBooleanField()
    isspecial = models.NullBooleanField()
    level = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=1000, blank=True, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    income = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usertype = models.CharField(max_length=20, blank=True, null=True)
    contract = models.CharField(max_length=50, blank=True, null=True)
    companyname = models.CharField(max_length=100, blank=True, null=True)
    jobposition = models.CharField(max_length=100, blank=True, null=True)
    card = models.CharField(max_length=100, blank=True, null=True)
    noaccept = models.CharField(max_length=500, blank=True, null=True)
    cprovince = models.CharField(max_length=100, blank=True, null=True)
    ccity = models.CharField(max_length=100, blank=True, null=True)
    cdistrict = models.CharField(max_length=100, blank=True, null=True)
    caddress = models.CharField(max_length=200, blank=True, null=True)
    abstracts = models.CharField(max_length=500, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_user_profile'
        ordering = ['-createtime']

    def __str__(self):
        if not self.realname:
            return self.pk_user
        return self.realname



class AppUserRewards(models.Model):
    pk_reward = models.CharField(primary_key=True,  default=get_uuid(),max_length=40)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    relateid = models.CharField(max_length=40, blank=True, null=True)
    relateobj = models.CharField(max_length=20, blank=True, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_user_rewards'


class AppUserverifyAudit(models.Model):
    pk_audit = models.CharField(primary_key=True,  default=get_uuid(),max_length=40)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    auditstatus = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=1000, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    audittime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_userverify_audit'
