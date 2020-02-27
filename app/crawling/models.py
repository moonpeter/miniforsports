from django.db import models


class CrawlingData(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
