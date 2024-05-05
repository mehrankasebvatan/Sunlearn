from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=110)
    image = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, default="")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey("Person", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField(default=0)
    website_address = models.URLField(default="")

    def __str__(self):
        return self.first_name + " " + self.last_name
