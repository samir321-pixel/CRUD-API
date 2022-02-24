from django.db import models


# Create your models here.


class user_data(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    zip = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=False, null=False)
    web = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-first_name']  # Sort in desc order
