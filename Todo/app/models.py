from django.db import models

class Todo(models.Model):
    title=models.CharField(max_length=100)
    detail=models.CharField(max_length=100)
    startdate=models.DateField()
    enddate=models.DateField()

    def __str__(self):
        return self.title
    

