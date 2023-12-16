from django.contrib import admin
from django.urls import include, path

from . import apis

urlpatterns = [
	path('get/<emp_no>', apis.GetEmployee),
]
