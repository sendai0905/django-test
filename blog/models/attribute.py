from django.db import models


class User(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name
