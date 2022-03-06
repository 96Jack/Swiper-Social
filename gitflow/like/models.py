from django.db import models

# Create your models here.

class Like(models.Model):
    uid = models.IntegerFiled()
    name = models.CharField()
    other_id = models.IntegerField()
    other_name = models.CharField()



