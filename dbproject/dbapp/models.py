from django.db import models

class Dbapp(models.Model):
    text = models.TextField()
    def __str__(self):
         return self.text
