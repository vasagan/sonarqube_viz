from django.shortcuts import render
# Create your views here.
#from django.conf import settings
import requests
from datetime import datetime, timezone, timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dateutil.parser import parse
from dateutil.relativedelta import *
from components.models import Components
import json
from . import login as sonarqube


@api_view(['GET'])
def chart(request, component_id, start_date, end_date):
    start_date = parse(start_date)
    end_date = parse(end_date)
    diff = relativedelta(start_date, end_date)
    date_levels =[end_date.isoformat()]
    for i in range(5):
        current_diff = diff*(i+1)
        date_level= (end_date+current_diff).isoformat()
        date_levels.insert(0, date_level)

    metrics = "directories,files,ncloc,classes,functions,comment_lines_density,sqale_index,violations,blocker_violations," \
              "critical_violations,major_violations,minor_violations,complexity,branch_coverage,line_coverage,coverage,tests,test_errors,comment_lines"
    fromDate = (start_date+(diff*5)).isoformat()
    s = sonarqube.get_session()
    #s.auth = (settings.SONAR_USERNAME, settings.SONAR_PASSWORD)
    url = 'https://sonar.sabre.com/api/timemachine/index?resource='+component_id+'&metrics='+metrics+'&fromDateTime='+ fromDate + '&toDateTime=' + end_date.isoformat()
    try:
        api_response = s.get(url, timeout=(6, 15))  # connection timeout =6 and response timeout = 15 seconds
    except requests.exceptions.Timeout as e:
        resp = {'error': 'sonar.sabre.com seems to be slow. Pls try again'}
        return Response(resp)

    js=api_response.json()
    items = js[0]["cells"]
    if items:
        total_items = len(items)
        date_level_values = []
        for level in date_levels:
            item_value=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            for item in items:
                if parse(item["d"])<= parse(level):
                    data = item["v"]
                    for i in range(len(data)):
                        if data[i] is None:
                            data[i]=0
                    item_value = [data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18]]
                else:
                    break
            date_level_values.append(item_value)

        tech_debt = [['Timeline', 'Technical Debt (Hours)','Lines of code']]
        complexity = [['Timeline', 'Complexity']]
        coverage = [['Timelines', 'Condition Coverage', 'Line Coverage', 'Overall Coverage']]
        unit_tests = [['Timeline', 'Total Unit Tests','Failed Unit Tests']]
        overall_progress = [['Timeline', 'Files', 'classes', 'functions','Comment Lines']]
        for i in range(6):
            parsed_date = parse(date_levels[i]).strftime('%d %b %y')
            tech_debt.append([parsed_date, (date_level_values[i][6])//60, date_level_values[i][2]])
            complexity.append([parsed_date, date_level_values[i][12]])
            coverage.append([parsed_date, date_level_values[i][13], date_level_values[i][14], date_level_values[i][15]])
            unit_tests.append([parsed_date, date_level_values[i][16], date_level_values[i][17]])
            overall_progress.append([parsed_date,date_level_values[i][1],date_level_values[i][3],date_level_values[i][4],date_level_values[i][18]])

        date_level_len = len(date_levels)
        data_level_values_len = len(date_level_values)
        date_one= parse(date_levels[date_level_len-2]).strftime('%d %b %y')
        date_two = parse(date_levels[date_level_len-1]).strftime('%d %b %y')

        last_item = date_level_values[data_level_values_len - 1]
        meta_data = [last_item[0], last_item[1], last_item[2], last_item[3], last_item[4], last_item[5]]

        violations = [['Violations', date_one, date_two]]
       # violations.append(['Total', date_level_values[data_level_values_len-2][2], date_level_values[data_level_values_len-1][2]])
        violations.append(['Blocker', date_level_values[data_level_values_len - 2][8], date_level_values[data_level_values_len - 1][8]])
        violations.append(['Critical', date_level_values[data_level_values_len - 2][9],date_level_values[data_level_values_len - 1][9]])
        violations.append(['Major', date_level_values[data_level_values_len - 2][10],date_level_values[data_level_values_len - 1][10]])
        violations.append(['Minor', date_level_values[data_level_values_len - 2][11],date_level_values[data_level_values_len - 1][11]])


        resp= {'meta': meta_data, 'tech_debt':tech_debt, 'violations': violations, 'complexity': complexity, 'coverage': coverage, 'unit_tests': unit_tests, 'overall': overall_progress}
    else:
        resp={'error': 'No data returned for the time period'}

    return Response(resp)
