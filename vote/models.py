#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django_openid_auth.models import User


class New(models.Model):
    title = models.CharField(max_length=20)
    pubtime = models.DateTimeField(auto_now_add=True)
    ups = models.IntegerField(default=0)
    downs = models.IntegerField(default=0)
    hot = models.FloatField(default=0)

    def __unicode__(self):
        return u'%d' % self.id


class UserVote(models.Model):
    user = models.ForeignKey(User)
    new = models.ForeignKey(New)
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    ipad = models.CharField(max_length=130)
