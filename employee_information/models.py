from datetime import datetime
from email.policy import default
from tabnanny import verbose
from django.db import models
from django.utils import timezone
from account.models import User
from garden.models import Ward

# Create your models here.
class Department(models.Model):
    job_id = models.AutoField(primary_key=True, unique=True,verbose_name='Job ID')
    job_dept = models.CharField(max_length=50,verbose_name='Job Department')
    name = models.CharField(max_length=50,verbose_name='Name') 
    description = models.TextField(verbose_name='Description')  
    date_added = models.DateTimeField(default=timezone.now, verbose_name='Date Added') 
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated') 

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Department"

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)

class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='User') 
    employee_id = models.AutoField(primary_key=True, unique=True, verbose_name='Employee ID') 
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0, verbose_name='Gender') 
    dob = models.DateField(blank=True,null= True, verbose_name='Date of Birth') 
    contact_no = models.CharField(max_length = 12, verbose_name='Contact Number') 
    address = models.TextField(verbose_name='Address') 
    department_id = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name='Department') 
    date_hired = models.DateField(verbose_name='Date Hired')
    status = models.BooleanField(default=True, verbose_name='Status') 
    date_added = models.DateTimeField(default=timezone.now, verbose_name='Date Added') 
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated') 

    def __str__(self):
        return '{} {}'.format(self.user.firstname, self.user.lastname )
    
    class Meta:
        verbose_name_plural = "Employees"


LEAVE_TYPE_CHOICES = (
    (0, 'Privilege Leave (PL)'),
    (1, 'Casual Leave (CL)'),
    (2, 'Sick Leave (SL)'),
    (3, 'Maternity Leave (ML)'),
    (4, 'Paternity Leave (PL)'),
    (5, 'Emergency Leave (EL)'),
    (6, 'Vacation Leave (VL)'),
    (7, 'Special Leave (SL)'),
)
      
class Leave(models.Model):
    leave_id = models.AutoField(primary_key=True, unique=True, verbose_name='Leave ID')
    emp_id = models.ForeignKey(Employees, on_delete=models.PROTECT, verbose_name='Employee ID')
    leave_type = models.IntegerField(choices=LEAVE_TYPE_CHOICES, default=0, verbose_name='Leave Type')
    reason = models.TextField(verbose_name='Reason')
    date_from = models.DateField(verbose_name='Date From')
    date_to = models.DateField(verbose_name='Date To')
    status_choices = [
        (1, 'Pending'),
        (2, 'Approved'),
        (3, 'Rejected'),
        (4, 'Cancelled')
    ]
    status = models.IntegerField(choices=status_choices, default=1,verbose_name='Status')
    date_applied = models.DateField(auto_now_add=True,verbose_name='Date Applied')
    
    def __str__(self):
        return '{}-{}'.format(self.leave_id, self.emp_id)
    
    class Meta:
        verbose_name_plural = "Leave"


class Worker(models.Model):
    worker_id = models.AutoField(primary_key=True, unique=True, verbose_name='Worker ID')
    emp_id = models.OneToOneField(Employees, on_delete=models.PROTECT, verbose_name='Employee ID')
    ward_id = models.ManyToManyField(Ward, verbose_name='Ward ID')
    date_added = models.DateTimeField(default=timezone.now, verbose_name='Date Added') 
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated') 

    def __str__(self):
        return '{}'.format(self.emp_id)
    
    class Meta:
        verbose_name_plural = "Worker"

    
