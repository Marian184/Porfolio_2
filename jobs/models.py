from django.db import models
from datetime import datetime
from django.utils.timezone import now
# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    company = models.CharField(max_length=200, default="")
    job_date = models.DateTimeField(null=True, blank=True)
    technologies = models.TextField(default="")

    def job_date_short(self):
        return self.job_date.strftime('%b %e %Y')