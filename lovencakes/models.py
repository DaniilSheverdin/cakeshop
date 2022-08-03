from pyexpat import model
from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.urls import reverse

class Category(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)

	class Meta:
		verbose_name_plural = 'категории'
	
	def __str__(self):
		return self.name

class Product(models.Model):
	category=models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, blank=True)
	title=models.CharField(max_length=255)
	description=models.TextField(blank=True)
	image=models.ImageField(upload_to='images/')
	slug=models.SlugField(max_length=255, unique=True)
	price=models.DecimalField(max_digits=5, decimal_places=2)
	in_stock=models.BooleanField(default=True)
	created=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural='Товары'
		ordering=('-created',)

	def __str__(self):
		return self.title