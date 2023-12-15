from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.utils import timezone

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from apps.employees import models as EmployeesModels

import json
import datetime

@csrf_exempt
@require_http_methods(["GET"])
def EmployeeGetTitles(request):
	if not request.user.is_authenticated: return HttpResponse(status=401)
	emp_no     = request.GET.get('emp_no')
	title_objs = EmployeesModels.Titles.objects.filter(emp_no=emp_no)
	return JsonResponse({"titles": list(map(lambda x: x.dict(), title_objs))})

@csrf_exempt
@require_http_methods(["GET"])
def EmployeeGetSalaries(request):
	if not request.user.is_authenticated: return HttpResponse(status=401)
	emp_no     = request.GET.get('emp_no')
	salary_objs = EmployeesModels.Salaries.objects.filter(emp_no=emp_no)
	return JsonResponse({"salaries": list(map(lambda x: x.dict(), salary_objs))})
