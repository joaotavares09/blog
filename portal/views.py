from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .forms import PostForm, AreaForm
from .models import Noticia
from .models import Area

def inicio(request):
	try:
		area_verde= Area.objects.get(cor="verde", status=True)
		noticias_esporte = Noticia.objects.filter(area=area_verde)
	except:
		noticias_esporte = []
	try:	
		area_vermelha= Area.objects.get(cor="vermelha", status=True)
		noticias_politica = Noticia.objects.filter(area=area_vermelha)
	except:
		noticias_politica = []
	return render(request, 'portal/inicio.html', {'noticias_politica': noticias_politica, 'noticias_esporte': noticias_esporte})

def area_list(request):
	posts = Noticia.objects.filter()#published_date__lte=timezone()
	return render(request, 'portal/post_list.html', {'posts': posts})

def area_post_list(request):
	posts = Area.objects.filter()#published_date__lte=timezone()
	return render(request, 'portal/area_post_list.html', {'posts': posts})

def area_detail(request, pk):
	post = get_object_or_404(Noticia, pk=pk)
	return render(request, 'portal/post_detail.html', {'post': post})

def area_post_detail(request, pk):
	post = get_object_or_404(Area, pk=pk)
	return render(request, 'portal/area_post_detail.html', {'post': post})

def area_new(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			#post.published_date = timezone.now()
			post.save()
			return redirect('area_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'portal/post_edit.html', {'form': form})

def area_post_new(request):
	if request.method == "POST":
		form = AreaForm(request.POST, request.FILES)
		if form.is_valid():
			area = form.save(commit=False)
			area.author = request.user
			#post.published_date = timezone.now()
			area.save()
			return redirect('area_post_detail', pk=area.pk)
	else:
		form = AreaForm()
	return render(request, 'portal/area_post_edit.html', {'form': form})

def area_edit(request, pk):
	post = get_object_or_404(Noticia, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			#post.published_date = timezone.now()
			post.save()
			return redirect('area_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'portal/post_edit.html', {'form': form})

def area_post_edit(request, pk):
	area = get_object_or_404(Area, pk=pk)
	if request.method == "POST":
		form = AreaForm(request.POST, request.FILES, instance=area)
		if form.is_valid():
			area = form.save(commit=False)
			area.author = request.user
			#post.published_date = timezone.now()
			area.save()
			return redirect('area_post_detail', pk=area.pk)
	else:
		form = AreaForm(instance=area)
	return render(request, 'portal/area_post_edit.html', {'form': form})

def area_publicar(request, pk):
	post = get_object_or_404(Noticia, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('area_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'portal/post_edit.html', {'form': form})

def area_remove(request, pk):
	post = get_object_or_404(Noticia, pk=pk)
	post.delete()
	return redirect('area_list')

def area_post_remove(request, pk):
	post = get_object_or_404(Area, pk=pk)
	post.delete()
	return redirect('area_post_list')