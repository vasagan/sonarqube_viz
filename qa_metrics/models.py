from django.db import models

# Create your models here.

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200)
    remarks = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


class Quality_metric(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    as_on_date = models.DateTimeField()
    sabre_defects_open = models.IntegerField()
    customer_defects_open = models.IntegerField()
    internal_defects_backlog = models.IntegerField()
    customer_defects_backlog = models.IntegerField()
    automatic_test_cases = models.IntegerField()
    manual_test_cases = models.IntegerField()
    functional_coverage = models.IntegerField()

    def __str__(self):
        return self.project.project_name
