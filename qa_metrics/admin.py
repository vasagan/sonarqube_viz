from django.contrib import admin
from qa_metrics.models import Project, Quality_metric

# Register your models here.


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ( 'project_id','project_name', 'updated_on', 'remarks')
    list_filter = ( 'project_name', 'updated_on', 'remarks')

class QaMetricsAdmin(admin.ModelAdmin):
    list_display = ( 'project', 'as_on_date', 'sabre_defects_open', 'customer_defects_open', 'internal_defects_backlog', 'customer_defects_backlog', 'automatic_test_cases', 'manual_test_cases', 'functional_coverage')
    list_filter = ( 'project', 'as_on_date', 'functional_coverage')

admin.site.register(Project, ProjectsAdmin)
admin.site.register(Quality_metric, QaMetricsAdmin)