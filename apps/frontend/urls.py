from django.contrib import admin
from django.urls import include, path

from apps.frontend import views as FrontendViews

urlpatterns = [
	path('', FrontendViews.employees),
	path('employee/<emp_no>', FrontendViews.employee_detail),
	path('departments/', FrontendViews.departments),
]
