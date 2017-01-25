from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from components.models import Components



def home(request):
    components = list(Components.objects.values())
    current_comp = components[0]
    return render(request, 'production/index.html',{'components': components, 'current_comp': current_comp})


def component_home(request, comp_id):
    components = list(Components.objects.values())
    current_comp = list(Components.objects.values().filter(project_id= comp_id))[0]
    return render(request, 'production/index.html',{'components': components, 'current_comp': current_comp})