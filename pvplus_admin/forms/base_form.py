# coding: utf-8
from django import forms
from django.db.models import Q

from pvplus_model.models.perspect import AppPerspects, AppPerspectComments
from pvplus_model.models.question import AppQuestions
from pvplus_model.models.stock import AppStock
from pvplus_model.models.user import AppUserProfile


def get_users(is_verified=False):
    """获取用户列表"""
    users = AppUserProfile.objects.all()
    if is_verified:  # 认证用户
        users = users.filter(isverified=True)

    return users


def get_stocks():
    """获取股票列表"""
    return AppStock.objects.filter(isdisabled=True)


def get_question():
    """获取提问列表"""
    return AppQuestions.objects.filter(Q(isaudited=True) & Q(isopen=True))


def get_perspects():
    """获取决议列表"""
    return AppPerspects.objects.filter(isaudited=True)


def get_perspect_comments():
    """获取决议评论列表"""
    return  AppPerspectComments.objects.filter(isaudited=True)


class AuthorForm(forms.Form):
    pk_user = forms.ModelChoiceField(queryset=get_users(), label='用户')
