from django.db import models

# Create your models here.
class Book(models.Model):
	name = models.CharField(max_length=100)
	abstract = models.TextField()

	def __str__(self):
		return self.name


class Chapter(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	abstract = models.TextField()