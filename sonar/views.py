from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from components.models import Components
from qa_metrics.models import Project


def home(request):
    components = list(Components.objects.values())
    current_comp = components[0]
    projects_list = list(Project.objects.all())
    return render(request, 'production/qa_metrics_home.html',
                  {'components': components, 'current_comp': current_comp, 'server_name': settings.SERVER_NAME,
                   'projects_list': projects_list})


def component_home(request, comp_id):
    components = list(Components.objects.values())
    current_comp = list(Components.objects.values().filter(project_id= comp_id))[0]
    return render(request, 'production/index.html',{'components': components, 'current_comp': current_comp, 'server_name': settings.SERVER_NAME})
