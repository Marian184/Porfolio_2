from django.db import models
from datetime import datetime
from django.utils.timezone import now
# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    company = models.CharField(max_length=200, default="")
    str_job_date = models.DateTimeField(null=True, blank=True)
    end_job_date = models.DateTimeField(null=True, blank=True)
    technologies = models.TextField(default="", blank=True)
    position = models.CharField(max_length=200, default="")
    responsibilities = models.TextField(default="", blank=True)

    def __str__(self):
        return self.company

    def job_date_start(self):
        return self.str_job_date.strftime('%b %Y')

    def job_date_end(self):
        return self.end_job_date.strftime('%b %e %Y')