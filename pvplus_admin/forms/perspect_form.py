# coding: utf-8
from django import forms

from pvplus_model.models.perspect import AppPerspects, AppPerspectComments
from pvplus_admin.forms import base_form


class PerspectForm(forms.ModelForm, base_form.AuthorForm):
    pk_stock = forms.ModelChoiceField(queryset=base_form.get_stocks(), label='股票')

    class Meta:
        model = AppPerspects
        exclude = ('',)


class PerspectCommentForm(forms.ModelForm, base_form.AuthorForm):
    pk_perspect = forms.ModelChoiceField(queryset=base_form.get_perspects(), label='决议')
    atuserid = forms.ModelChoiceField(queryset=base_form.get_users(), label='@用户')
    atcommentid = forms.ModelChoiceField(queryset=base_form.get_perspect_comments(), label='@评论')

    class Meta:
        model = AppPerspectComments
        exclude = ('',)
