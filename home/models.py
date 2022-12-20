from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.


class Head(models.Model):
    trade_price = models.FloatField()
    hour_price = models.FloatField()
    volume = models.FloatField()

    # def __str__(self):
    #     return self.trade_price


class About(models.Model):
    title = models.CharField(max_length=255)
    about_image = models.ImageField(upload_to='photos', blank=True)
    about_title = models.CharField(max_length=255)
    about_description = RichTextField()
    market_captilization = models.FloatField(blank=True)
    daily_transaction = models.FloatField(blank=True)
    active_accounts = models.IntegerField(blank=True)
    years = models.IntegerField(blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    article_text = RichTextField()
    article_photo = models.ImageField(upload_to='photos', blank=True)
    article_description = RichTextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    no_of_comments = models.IntegerField()
    tags = models.CharField(max_length=255)

    def __str__(self):
        return self.article_text
