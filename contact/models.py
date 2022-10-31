from django.db import models

# Create your models here.


class Contact(models.Model):

	class Meta:
		verbose_name_plural = 'Contact List'

	name = models.CharField(max_length=150)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.TextField()
	
	def __str__(self):
		return self.subject