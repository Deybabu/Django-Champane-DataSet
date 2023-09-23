from django.db import models


class DateRange(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
