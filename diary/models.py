from django.db import models
from django.conf import settings


class Log(models.Model):
    create_date = models.DateTimeField('create date', auto_now_add=True)
    content = models.TextField('content', blank=False)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "log"
        verbose_name_plural = "logs"
