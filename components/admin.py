from django.contrib import admin
from components.models import Components, TestCases

# Register your models here.


class ComponenetsAdmin(admin.ModelAdmin):
    list_display = ( 'project_name', 'project_id', 'project_key', 'project_sonar_url')

class TestCasesAdmin(admin.ModelAdmin):
    list_display = ( 'comp_id', 'automatic', 'manual', 'as_on_date')

admin.site.register(Components, ComponenetsAdmin)
admin.site.register(TestCases, TestCasesAdmin)