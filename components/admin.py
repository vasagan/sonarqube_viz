from django.contrib import admin
from components.models import Components

# Register your models here.


class ComponenetsAdmin(admin.ModelAdmin):
    list_display = ( 'project_name', 'project_id', 'project_key', 'project_sonar_url')


admin.site.register(Components, ComponenetsAdmin)
