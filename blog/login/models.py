from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название роли")

    def __str__(self):
        return self.name

class User(models.Model):
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    balance = models.FloatField(default=0.0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.login