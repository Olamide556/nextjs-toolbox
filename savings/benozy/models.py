from django.db import models


class SavingCalc(models.Model):
    saved_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20, null=False)
    day = models.CharField(max_length=30, null=False)
    month = models.CharField(max_length=30, null=False)
    is_paid = models.BooleanField(default=False)
    price = models.IntegerField(null=True)
    time_hour = models.IntegerField(null=True)
    time_min= models.IntegerField(null=True)

    def __str__(self):
        return f'order: {self.saved_on.strftime("%b %d %I: %M %p")}'



