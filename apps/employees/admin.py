from django.contrib import admin
from django.utils.html import format_html

from . import models

class EmployeesAdmin(admin.ModelAdmin):
	list_display = ('emp_no', 'first_name', 'last_name', 'gender', 'birth_date', 'hire_date')
	ordering = ('emp_no',)
	list_filter = ('gender',)
	search_fields = ('emp_no','first_name','last_name')
	change_form_template = 'employees_employee_change_form.html'
admin.site.register(models.Employees, EmployeesAdmin)

class DepartmentsAdmin(admin.ModelAdmin):
	list_display = ('dept_no', 'dept_name')
	ordering = ('dept_no',)
admin.site.register(models.Departments, DepartmentsAdmin)

class SalariesAdmin(admin.ModelAdmin):
	list_display = ('emp_no', 'salary','from_date','to_date')
	ordering = ('emp_no',)
admin.site.register(models.Salaries, SalariesAdmin)

class TitlesAdmin(admin.ModelAdmin):
	def _action(self, obj): return ''
	_action.short_description = ""

	def _employee(self, obj):
		employee = models.Employees.objects.get(emp_no=obj.emp_no.emp_no)
		return f'{employee.first_name} {employee.last_name}'
	_employee.short_description = "Employee"

	# def _emp(self, obj): return format_html(f'<a href="#">{obj.emp_no}</a>')
	# _emp.short_description = "Employee"
	# _emp.admin_order_field = ''

	list_display = ('_action', '_employee', 'title','from_date','to_date')
	# ordering = ('_emp',)
	list_filter = ('title',)
admin.site.register(models.Titles, TitlesAdmin)