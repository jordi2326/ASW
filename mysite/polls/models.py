from django.db import models


class Usuari (model.Model):
	Title =models.CharField(max_length=200)
	T=models.CharField(max_length=200)
	P=models.CharField(max_length=200)
	Status=models.CharField(max_length=200)
	Votes=models.CharField(max_length=200)
	Asignee=models.TextField(max_length=200)
	Created=models.DataTimeField('date Created')
	Update=models.DataTimeField('date Update')

class Choice (models.Model):
	question = models.ForeignKey()

		