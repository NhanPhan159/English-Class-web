from enum import unique
from django.db import models
from api_class.models import Class
# Create your models here.
class classDetail(models.Model):
    option = [("am","AM"),("pm","PM"),("eve","EVE")]
    begin = models.TimeField(auto_now=False, auto_now_add=False)
    end = models.TimeField(auto_now=False, auto_now_add=False)
    session = models.CharField(choices=option,max_length=4,default="")
    id_class = models.ForeignKey(Class,on_delete=models.CASCADE)
    class Meta:
        unique_together = ["begin","end","session"]
