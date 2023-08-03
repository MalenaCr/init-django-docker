from django.db import models

# Create your models here.
from django.utils import timezone
class Task(models.Model):
    title = models.CharField(max_lengh= 180)
    description: models.TewtField(null=true, blank=True)
    priority= models.IntegerField(choises=((0, 'low'), (1, 'medium'), (2, 'high')))
    created_at = models.DateTiimeField(default=timezone.now)
    expired_at= models.DateTimeField(null=True, black=True)

