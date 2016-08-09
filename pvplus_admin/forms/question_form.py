# coding: utf-8
from django import forms
from django.db.models import Q

from pvplus_model.models.question import AppQuestions, AppAnswers, AppListens
from pvplus_admin.forms import base_form

YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
)


class QuestionForm(forms.ModelForm):
    # pk_user = forms.ChoiceField(choices=base_form.get_users(), label=u'提问用户')
    pk_user=forms.ModelChoiceField(queryset=base_form.get_users(),label='提问用户')

    pk_respondent = forms.ModelChoiceField(queryset=base_form.get_users(True), label=u'回答用户')

    class Meta:
        model = AppQuestions
        exclude = ('',)

        # def __init__(self, *args, **kwargs):
        #     initial = kwargs.get('initial', {})
        #     instance = kwargs.get('instance')
        #     if instance:
        #         # initial['user'] = AppUserProfile.objects.filter(pk_user=instance.pk_user).values_list('pk_user','realname')[0]
        #         initial['user'] = instance.pk_user
        #         initial['respondent'] = instance.pk_respondent
        #         super(QuestionForm, self).__init__(initial=initial, *args, **kwargs)
        #     else:
        #         super(QuestionForm, self).__init__(*args, **kwargs)


class AnswerForm(forms.ModelForm, base_form.AuthorForm):
    pk_question = forms.ModelChoiceField(queryset=base_form.get_question(), label='提问')

    class Meta:
        model = AppAnswers
        exclude = ('',)


class ListenForm(forms.ModelForm, base_form.AuthorForm):
    pk_question = forms.ModelChoiceField(queryset=base_form.get_question(), label='提问')

    class Meta:
        model = AppListens
        exclude = ('',)
