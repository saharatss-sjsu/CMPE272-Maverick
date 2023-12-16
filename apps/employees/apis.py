from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.utils import timezone

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from apps.employees import models as EmployeesModels

@csrf_exempt
@require_http_methods(["GET"])
def GetEmployee(request, emp_no):
	# if not request.user.is_authenticated: return HttpResponse(status=401)
	try:
		employee = EmployeesModels.Employees.objects.get(emp_no=emp_no)
		departments = EmployeesModels.DeptEmp.objects.filter(emp_no=emp_no).order_by('to_date')
		titles      = EmployeesModels.Titles.objects.filter(emp_no=emp_no).order_by('to_date')
		return JsonResponse({"employee": {
			**employee.dict(),
			'departments': [x.dict() for x in departments],
			'titles':      [x.dict() for x in titles],
		}})
	except EmployeesModels.Employees.DoesNotExist:
		return JsonResponse({"employee": None})
