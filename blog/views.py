from django.shortcuts import render
from .models import Post
from django.utls import timezone

def post_list(request):
	post = Post.objects.filter(published_date__lte=timezone.now())
	return render(request, 'blog/post_list.html', {'post': posts})