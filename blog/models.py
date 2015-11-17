from django.db import models
from django.db import permalink

# Create your models here.

class Blog(models.Model):
	Title  = models.CharField(max_length=100 unique=True)
	Slug =models.SlugFiels(max_length=100 unique=True)
	body = models.Textfield()
	posted= models.DateField(db_index=True, auto_now_add=True)
	category = models.ForeignKey('Blog.Category')

	def_unicode_(self):
	return '%s' %self.Title
	@permalink
	def_get_absolute_url(self):
	return ('view_blog_post',None,{'slug': self.slug})

	class Category(models.Model):
	Title = models.CharField(max_lenght=100 unique = True)
	Slug =models.SlugField(max_length=100 unique=True)

	def_unicode_(self):
	return'%s' %self.Title

	@permalink
	def_get_absolute_url(self):
	return('view_blog_category', None, {'slug': self.slug})

