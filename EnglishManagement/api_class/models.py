from django.db import models

# Create your models here.
class Class(models.Model):
    option = [(str(i),"Lớp "+str(i)) for i in range(1,13)]
    grade = models.CharField(max_length=2,default="10",choices=option)
    create = models.DateField(auto_now_add=True)
