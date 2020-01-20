from django.db import models
from django.utils import timezone
from django.conf import settings

class Area(models.Model):
	descricao = models.CharField(max_length=100)
	cor = models.CharField(max_length=100)
	status = models.BooleanField()

	def ativar(self):
		self.status = True
		self.save()

	def desativar(self):
		self.status = False
		self.save()

	def __str__(self):
		return self.descricao

class Noticia(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	area = models.ForeignKey('Area', on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	photo = models.ImageField(upload_to='imagens/', null=True, blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title