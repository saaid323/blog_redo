from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    context = { 'blogs': blogs}
    return render(request, 'base/index.html', context)

def CreateBlog(request):
    form = BlogForm()
    print(request.POST)
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
    context = { 'forms': form }
    return render(request, 'base/create.html', context)

def UpdateBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        form.save()
        return redirect("home")
    context = { 'forms': form }
    return render(request, 'base/create.html', context)

def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return redirect("home")
