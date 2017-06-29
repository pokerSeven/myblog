# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import  Article
from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_time')
    list_filter = ('pub_time',)
    pass

admin.site.register(Article,ArticleAdmin)
# Register your models here.
