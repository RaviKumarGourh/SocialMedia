from django.db import models

# Create your models here.
class UserTable(models.Model):
    username = models.CharField(primary_key=True,max_length = 50)
    password = models.CharField(max_length=50)
    realname = models.CharField(max_length=50)
class ConversationTable(models.Model):
    username = models.CharField(max_length = 50)
    message = models.CharField(max_length = 1000)


