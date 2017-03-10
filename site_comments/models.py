# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class SiteComments (models.Model):
    user = models.ForeignKey(User)
    dateCreated = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    url = models.CharField(max_length=200)
