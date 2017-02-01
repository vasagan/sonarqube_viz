from django.db import models

# Create your models here.


class Components(models.Model):
    project_id = models.IntegerField()
    project_key = models.CharField(max_length=200)
    project_name = models.CharField(max_length=200)
    project_sonar_url = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.project_name


