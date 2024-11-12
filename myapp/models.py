from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, default="?")
    family = models.CharField(max_length=100, null=False, blank=False, default="?")
    def __str__(self):
        return self.name + " " + self.family

class Book(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, default="?")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title
