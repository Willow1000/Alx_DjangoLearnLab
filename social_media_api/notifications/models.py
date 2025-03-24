from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from accounts.models import User
# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(User,on_delete=models.CASCADE)
    actor = models.ForeignKey(User,on_delete=models.CASCADE)
    verb = models.ForeignKey(User,on_delete=models.CASCADE)
    target = GenericForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)