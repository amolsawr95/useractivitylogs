
from django.utils import timezone
import pytz
from django.db import models


# Create your models here
class NewUser(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    real_name = models.CharField( max_length=50)
    tz = models.CharField( max_length=50)
 

    class Meta:
        verbose_name = ("NewUser")
        verbose_name_plural = ("NewUsers")


    @property
    def activity_periods(self):
        return self.activityperiod_set.all() 
    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    start_time = models.DateTimeField(  default=timezone.now)
    end_time = models.DateTimeField(  default=timezone.now)

    class Meta:
        verbose_name = ("ActivityPeriod")
        verbose_name_plural = ("ActivityPeriods")

