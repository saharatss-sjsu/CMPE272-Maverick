# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

GENDER = (
	('M','Male'),
	('F','Female')
)

class Departments(models.Model):
	dept_no = models.CharField(primary_key=True, max_length=4)
	dept_name = models.CharField(unique=True, max_length=40)
	class Meta:
		managed = False
		db_table = 'departments'
		verbose_name_plural = 'departments'
	def dict(self):
		return {
			'dept_no':self.dept_no,
			'dept_name':self.dept_name,
		}


class DeptEmp(models.Model):
	emp_no = models.OneToOneField('Employees', models.DO_NOTHING, db_column='emp_no', primary_key=True)
	dept_no = models.ForeignKey(Departments, models.DO_NOTHING, db_column='dept_no')
	from_date = models.DateField()
	to_date = models.DateField()
	class Meta:
		managed = False
		db_table = 'dept_emp'
		unique_together = (('emp_no', 'dept_no'),)
	def dict(self):
		return {
			'department': self.dept_no.dict(),
			'from_date': self.from_date,
			'to_date': self.to_date,
		}

class DeptManager(models.Model):
	emp_no = models.OneToOneField('Employees', models.DO_NOTHING, db_column='emp_no', primary_key=True)
	dept_no = models.ForeignKey(Departments, models.DO_NOTHING, db_column='dept_no')
	from_date = models.DateField()
	to_date = models.DateField()
	class Meta:
		managed = False
		db_table = 'dept_manager'
		unique_together = (('emp_no', 'dept_no'),)

class Employees(models.Model):
	emp_no = models.IntegerField(primary_key=True)
	birth_date = models.DateField()
	first_name = models.CharField(max_length=14)
	last_name = models.CharField(max_length=16)
	gender = models.CharField(max_length=1, choices=GENDER)
	hire_date = models.DateField()
	def __str__(self):
		return f"{self.first_name} {self.last_name}"
	class Meta:
		managed = False
		db_table = 'employees'
		verbose_name_plural = 'employees'
	def dict(self):
		return {
			'emp_no':         self.emp_no,
			'first_name':     self.first_name,
			'last_name':      self.last_name,
			'gender':         self.gender,
			'hire_date':      self.hire_date,
			'hire_date_iso':  self.hire_date.isoformat(),
			'birth_date':     self.birth_date,
			'birth_date_iso': self.birth_date.isoformat(),
		}


class Salaries(models.Model):
	emp_no = models.OneToOneField(Employees, models.DO_NOTHING, db_column='emp_no', primary_key=True)
	salary = models.IntegerField()
	from_date = models.DateField()
	to_date = models.DateField()
	class Meta:
		managed = False
		db_table = 'salaries'
		verbose_name_plural = 'salaries'
		unique_together = (('emp_no', 'from_date'),)
	def dict(self):
		return {
			'emp_no':self.emp_no.emp_no,
			'salary':self.salary,
			'from_date':self.from_date,
			'to_date':self.to_date,
		}


class Titles(models.Model):
	emp_no    = models.OneToOneField(Employees, models.DO_NOTHING, db_column='emp_no', primary_key=True)
	title     = models.CharField(max_length=50)
	from_date = models.DateField()
	to_date   = models.DateField(blank=True, null=True)
	class Meta:
		managed = False
		db_table = 'titles'
		verbose_name_plural = 'titles'
		unique_together = (('emp_no', 'title', 'from_date'),)
	def dict(self):
		return {
			'emp_no':self.emp_no.emp_no,
			'title':self.title,
			'from_date':self.from_date,
			'to_date':self.to_date,
		}