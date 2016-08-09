# coding: utf-8
from django.contrib import admin

# Register your models here.
from pvplus_admin.forms.question_form import QuestionForm, AnswerForm, ListenForm
from pvplus_admin.forms.perspect_form import PerspectForm, PerspectCommentForm
from pvplus_model.models.perspect import AppPerspects, AppPerspectComments
from pvplus_model.models.stock import AppStock
from pvplus_model.models.question import AppQuestions, AppAnswers, AppListens


@admin.register(AppQuestions)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk_question', 'content','createtime')
    fields = ('pk_user', 'questionmode', 'questionrelate', 'content', 'pk_respondent', 'question_price', 'listen_price',
              'listennum', 'goodnum', 'isopen', 'isaudited')
    # exclude = ('pk_user','pk_question','pk_respondent','status','updatetime')
    # raw_id_fields = ('pk_user',)
    form = QuestionForm

    def save_model(self, request, obj, form, change):
        # if not change:
        #     obj.pk_question = str(uuid.uuid1()).replace('-','')

        obj.pk_user = getattr(form.cleaned_data['pk_user'],'pk')
        obj.pk_respondent = getattr(form.cleaned_data['pk_respondent'],'pk')

        obj.save()


@admin.register(AppAnswers)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk_answer', 'voice', 'duration', 'content','createtime')
    fields = ('pk_user', 'pk_question', 'voice', 'duration', 'content', 'isbest')
    form = AnswerForm

    def save_model(self, request, obj, form, change):
        # if not change:
        #     obj.pk_question = str(uuid.uuid1()).replace('-','')

        obj.pk_user =getattr(form.cleaned_data['pk_user'],'pk')
        obj.pk_question =getattr(form.cleaned_data['pk_question'],'pk')

        obj.save()


@admin.register(AppListens)
class ListenAdmin(admin.ModelAdmin):
    list_display = ('pk_listen','pk_question','iscommented','createtime')
    exclude = ('pk_listen', 'createtime')
    form = ListenForm

    def save_model(self, request, obj, form, change):
        # if not change:
        #     obj.pk_question = str(uuid.uuid1()).replace('-','')

        obj.pk_user =getattr(form.cleaned_data['pk_user'],'pk')
        obj.pk_question = getattr(form.cleaned_data['pk_question'],'pk')

        obj.save()


@admin.register(AppStock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('pk_stock', 'stockname', 'tradetype', 'isdisabled', 'istop', 'sortno')
    exclude = ('createtime',)


@admin.register(AppPerspects)
class PerspectAdmin(admin.ModelAdmin):
    list_display = ('pk_perspect', 'pk_stock', 'title', 'stockprice', 'isbullish', 'isaudited','createtime')
    fields = ('pk_stock', 'pk_user', 'title', 'reason', 'stockprice', 'isbullish', 'expertprice', 'expertrate',
              'commentnum', 'goodnum', 'downnum', 'isaudited')
    form = PerspectForm

    def save_model(self, request, obj, form, change):
        # if not change:
        #     obj.pk_question = str(uuid.uuid1()).replace('-','')

        obj.pk_user = getattr(form.cleaned_data['pk_user'],'pk')
        obj.pk_stock = getattr(form.cleaned_data['pk_stock'],'pk')

        obj.save()


@admin.register(AppPerspectComments)
class PerspectCommentAdmin(admin.ModelAdmin):
    list_display = ('pk_comment','pk_perspect','content','isaudited','createtime')
    form = PerspectCommentForm
    exclude = ('pk_comment',)

    def save_model(self, request, obj, form, change):
        # if not change:
        #     obj.pk_question = str(uuid.uuid1()).replace('-','')

        obj.pk_user = getattr(form.cleaned_data['pk_user'], 'pk')
        obj.pk_perspect = getattr(form.cleaned_data['pk_perspect'],'pk')
        obj.atuserid = getattr(form.cleaned_data['atuserid'],'pk')
        obj.atcommentid = getattr(form.cleaned_data['atcommentid'], 'pk')

        obj.save()





    # admin.site.register(AppQuestions)
    # admin.site.register(AppAnswers)
    # admin.site.register(AppListens)
