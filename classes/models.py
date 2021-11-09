from django.db import models
from django.contrib.auth import get_user_model


class Class(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    start = models.DateField()
    end = models.DateField()
    students = models.ManyToManyField(get_user_model(), through='Registration')


class Registration(models.Model):
    data = models.DateField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    class_user = models.ForeignKey(Class, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user', 'class_user']]
        ordering = ['class_user', 'data']
