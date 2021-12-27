from django.db import models

class Info(models.Model):
    name=models.CharField(max_length=20)
    uid=models.IntegerField()
    email=models.EmailField(max_length=54)
    gender=models.CharField(max_length=10)
    location=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    obj=models.Manager()

    def __str__(self):
    	return self.name
       
    class Meta:
        db_table='info'