from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q

from apps.employees import models as EmployeeModels
import math

def staff_check(user):
	return user.is_staff

@login_required
@user_passes_test(staff_check, login_url='/logout/')
def employees(request):
	employees_order_by = request.GET.get('order_by')
	employees_order_list = ['emp_no', 'first_name', 'last_name', 'birth_date', 'hire_date']
	if employees_order_by not in employees_order_list: employees_order_by = 'emp_no'

	employees_order_ascending = request.GET.get('order_ascending', 'true') == 'true'

	# Lazyload all employee records
	employees = EmployeeModels.Employees.objects.all()

	# Search by ID or Name
	employees_search = request.GET.get('search')
	if employees_search is not None:
		employees = employees.filter(Q(emp_no__contains=employees_search) | Q(first_name__contains=employees_search) | Q(last_name__contains=employees_search))

	# Filter by department
	departments = [x.dict() for x in EmployeeModels.Departments.objects.all()]
	employees_filter_department = request.GET.get('filter_department')
	if employees_filter_department in [department['dept_no'] for department in departments]:
		employees = employees.filter(deptemp__dept_no=employees_filter_department)

	# Filter by job title
	titles = [x['title'] for x in EmployeeModels.Titles.objects.all().values('title').distinct()]
	employees_filter_title = request.GET.get('filter_title')
	if employees_filter_title in titles:
		employees = employees.filter(titles__title=employees_filter_title)

	# Filter by gender
	employees_filter_gender = request.GET.get('filter_gender')
	if employees_filter_gender in ['M','F']:
		employees = employees.filter(gender=employees_filter_gender)

	# Count after filter
	employees_count      = employees.count()

	# Sort
	employees            = employees.order_by(('' if employees_order_ascending else '-')+employees_order_by)

	# Paging
	employees_per_page   = 1000
	employees_page_index = int(request.GET.get('page', 1))
	employees_page_count = math.ceil(employees_count/employees_per_page)
	if employees_page_index < 1: employees_page_index = 1
	if employees_page_index > employees_page_count: employees_page_index = employees_page_count
	if employees.count() > employees_per_page:
		employees = employees[(employees_page_index-1)*employees_per_page : (employees_page_index)*employees_per_page]
	employees_page_size  = employees.count()

	return render(request, 'employees.html', {
		'departments':                 list(map(lambda x: x.dict(), EmployeeModels.Departments.objects.all())),
		'titles':                      titles,
		'employees':                   [{**x.dict(), 'index':((employees_page_index-1)*employees_per_page)+i+1} for i,x in enumerate(employees)],
		'employees_count':             employees_count,
		'employees_per_page':          employees_per_page,
		'employees_page_index':        employees_page_index,
		'employees_page_count':        employees_page_count,
		'employees_page_size':         employees_page_size,

		'employees_order_by':          employees_order_by,
		'employees_order_list':        employees_order_list,
		'employees_order_ascending':   employees_order_ascending,

		'employees_search':            employees_search,
		'employees_filter_department': employees_filter_department,
		'employees_filter_title':      employees_filter_title,
		'employees_filter_gender':     employees_filter_gender,
	})

@login_required
@user_passes_test(staff_check, login_url='/logout/')
def employee_detail(request, emp_no):
	employee = EmployeeModels.Employees.objects.get(emp_no=emp_no)
	return render(request, 'employee_detail.html', {
		'employee':    employee.dict(),
		'titles':      [x.dict() for x in EmployeeModels.Titles.objects.filter(emp_no=employee)],
		'salaries':    [x.dict() for x in EmployeeModels.Salaries.objects.filter(emp_no=employee)],
		'departments': [x.dict() for x in EmployeeModels.DeptEmp.objects.filter(emp_no=employee)],
	})

@login_required
@user_passes_test(staff_check, login_url='/logout/')
def departments(request):
	departments       = EmployeeModels.Departments.objects.all()
	departments_count = departments.count()
	return render(request, 'departments.html', {
		'departments':       [{**x.dict(), 'employees_count':EmployeeModels.DeptEmp.objects.filter(dept_no=x.dept_no).count()} for x in departments],
		'departments_count': departments_count,
	})