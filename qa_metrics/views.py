from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
import requests
from datetime import datetime, timezone, timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dateutil.parser import parse
from dateutil.relativedelta import *
from components.models import Components
from qa_metrics.models import Project, Quality_metric
import json






def qa_metrics_home(request):
    components = list(Components.objects.values())
    current_comp = components[0]
    projects_list = list(Project.objects.all())
    return render(request, 'production/qa_metrics_home.html',{'components': components, 'current_comp': current_comp, 'server_name': settings.SERVER_NAME, 'projects_list':projects_list})



@api_view(['GET'])
def qa_metrics_api(request, project_id, start_date, end_date):
    start_date = parse(start_date)
    end_date = parse(end_date)
    diff = relativedelta(start_date, end_date)
    date_levels =[end_date.isoformat()]
    for i in range(5):
        current_diff = diff*(i+1)
        date_level= (end_date+current_diff).isoformat()
        date_levels.insert(0, date_level)
    test_cases = Quality_metric.objects.all().filter(project=project_id, as_on_date__lte = end_date).order_by('as_on_date')
    if not test_cases:
        resp = { 'error': 'No data returned for the chosen period'}
        return Response(resp)
    date_level_values = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for test in test_cases:
        i=0
        for level in date_levels:
            if test.as_on_date <= parse(level):
                date_level_values[i]= [test.automatic_test_cases, test.manual_test_cases, test.automatic_test_cases+test.manual_test_cases, test.functional_coverage]
            i+=1
            continue
    test_case_numbers = [['Timeline', 'Automated', 'Manual']]
    automated_percentage = [['Timeline', 'Automation Percentage']]
    functional_coverage = [['Timeline', 'Functional Coverage']]
    for i in range(6):
        if date_level_values[i][2] != 0:
            automated_percent = (date_level_values[i][0]/date_level_values[i][2])*100
        else:
            automated_percent =0
        parsed_date = parse(date_levels[i]).strftime('%d %b %y')
        test_case_numbers.append(
            [parsed_date, date_level_values[i][0],
             date_level_values[i][1]])
        automated_percentage.append([parsed_date, automated_percent])
        functional_coverage.append([parsed_date, date_level_values[i][3]])

    resp = { 'test_cases' : test_case_numbers, 'automated_percentage': automated_percentage, 'functional_coverage': functional_coverage }
    return Response(resp)