from django.db import models


class NewsStore(models.Model):
    orginal_news = models.TextField(default="", blank=True, null=True)
    converted_news = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        return str(self.orginal_news)