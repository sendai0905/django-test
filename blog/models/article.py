from django.db import models
from blog.models.attribute import User, Category


class Article(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(max_length=5000)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # @property
    # def age(self):
    #     return Unko.objects.get(id=1)

    def __str__(self):
        return self.title


# class Unko(models.Model):
#     text = models.TextField(max_length=100)

#     def __str__(self):
#         return self.text
