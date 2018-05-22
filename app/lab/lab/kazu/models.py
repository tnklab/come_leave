from django.db import models


class Kazu(models.Model):
    content = models.CharField(max_length = 140,verbose_name = '本文')
    posted_date = models.DataTimeField(auto_now_add = True)



# Create your models here.
