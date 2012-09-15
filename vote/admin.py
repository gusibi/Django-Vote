#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from vote.models import New, UserVote


class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'pubtime', 'ups', 'downs', 'hot')


class UserVoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'up', 'down', 'ipad')


admin.site.register(New, NewAdmin)
admin.site.register(UserVote, UserVoteAdmin)
