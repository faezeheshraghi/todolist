from django.db import models

# Create your models here.

class To_Do_List(models.Model):
    list_id = models.CharField(max_length=250, blank=True)
    titel = models.CharField(max_length=100, blank=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=250,blank=True)

    def __str__(self):
        return self.list_id
