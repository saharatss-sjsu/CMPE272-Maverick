from django.contrib import admin

from . import models

class EmployeesAdmin(admin.ModelAdmin):
	list_display = ('emp_no', 'first_name', 'last_name', 'gender', 'birth_date', 'hire_date')
	ordering = ('emp_no',)
	list_filter = ('gender',)
admin.site.register(models.Employees, EmployeesAdmin)

class DepartmentsAdmin(admin.ModelAdmin):
	list_display = ('dept_no', 'dept_name')
	ordering = ('dept_no',)
admin.site.register(models.Departments, DepartmentsAdmin)

# class SalariesAdmin(admin.ModelAdmin):
# 	list_display = ('emp_no', 'salary','from_date','to_date')
# 	ordering = ('emp_no',)
# admin.site.register(models.Salaries, SalariesAdmin)

class TitlesAdmin(admin.ModelAdmin):
	list_display = ('emp_no', 'title','from_date','to_date')
	ordering = ('emp_no',)
admin.site.register(models.Titles, TitlesAdmin)