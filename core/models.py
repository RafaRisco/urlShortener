import random, string
import requests
from django.core.exceptions import ValidationError
from django.db import models
from lxml.html import fromstring
import validators
# Create your models here.


validators.url("http://google.com")

def validate_url(url):
    if not validators.url(url):
        raise ValidationError(f"{url} is not an even number")

class ShortsUrl(models.Model):

    url = models.TextField(unique=True, validators=[validate_url])
    short_url = models.CharField(max_length=200, blank=True, null=True, unique=True)
    counter = models.PositiveBigIntegerField(default=0)
    web_title = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.short_url
    
    def save(self, *args, **kwargs):
        if not self.web_title:
            r = requests.get(f'{self.url}')
            tree = fromstring(r.content)
            self.web_title = tree.findtext('.//title')
        if not self.short_url:
            valid_short_url = False
            while not valid_short_url:
                short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                existing_short_url = self.__class__.objects.filter(short_url=short_url)
                if not existing_short_url:
                    valid_short_url = True
            # Check the short_url does not already exists
            self.short_url = short_url
        super(ShortsUrl, self).save(*args, **kwargs)