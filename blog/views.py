from django.shortcuts import render_to_response, get_object_or_404

from django.blog.models import Blog , Category
# Create your views here.


def index(request):
	return render_to_response('index.html',{
	'Categories':Category.objects.all(),
	'Posts':Blog.objects.all()[5]})

def view_post(request, slug):
	return render_to_response('view_post.html',{
	'post':get_object_or_404(Blog,slug=slug) })

def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('view_category.html',{
	'Category':category,
	'posts':Blog.objects.filter(category=category)[5]})
