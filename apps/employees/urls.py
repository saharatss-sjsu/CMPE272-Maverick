from django.urls import include, path

from . import apis

urlpatterns = [
	path("gettitles/", apis.EmployeeGetTitles),
	path("getsalaries/", apis.EmployeeGetSalaries),
]