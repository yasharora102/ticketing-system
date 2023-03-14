from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Staff(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,null=True )

    def __str__(self):
        return self.user.username

    
class Ticket(models.Model):
    created_by = models.ForeignKey(Staff, related_name="created_by", on_delete=models.SET_NULL, null=True)
    assigned_to = models.ForeignKey(Staff, related_name="assigned_to", on_delete=models.SET_NULL, null=True)
    department_id = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    STATUS_CHOICES = (
        ("Open", "Open"),
        ("Closed", "Closed"),
    )
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default="Open")

    priority = models.IntegerField() 

    def __str__(self):

        return self.title
