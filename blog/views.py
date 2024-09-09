from django.shortcuts import render, redirect
from .models import Post, Author,Comment
from .forms import PostForm, CommentForm, UserForm, AuthorForm, UpdateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http.response import HttpResponse
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.

def post_list(request):
    q = request.GET.get('q', '')
    posts = Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    return render(request, 'blog/post_list.html', {"posts": posts})

def post_detail(request, pk):
    read_blogs_id =  request.session.get('read_blog',[])
    if 'read_blog' not in request.session:
        request.session['read_blog'] = []
    if pk not in read_blogs_id:
        request.session['read_blog'].insert(0, pk)
        request.session.modified = True
    post = Post.objects.get(pk=pk)
    comments = post.comments.all()
    form = CommentForm()
    context = {'post': post, "form": form, "comments": comments}
    return render(request, 'blog/post_detail.html', context)


def update_post(request, pk):
    blog = Post.objects.get(id=pk)
    form = PostForm(instance=blog)
    if request.method == 'POST':
        form = PostForm(request.POST,  request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk)
    context = { 'form': form }
    return render(request, "blog/post_create.html", context)


def delete_post(request, pk):
    blog = Post.objects.get(id=pk)
    blog.delete()
    HttpResponse()

def user_history(request):
    read_blog_ids = request.session.get('read_blog', [])[::-1]
    read_history = Post.objects.filter(id__in=read_blog_ids).order_by('id')
    context = {'read_history': read_history}
    return render(request, 'history.html', context)


def delete_read_history(request, pk):
    read_blog_ids = request.session.get('read_blog', [])
    if pk in read_blog_ids:
        read_blog_ids.remove(pk)
        request.session['read_blog'] = read_blog_ids
        request.session.modified = True
    return redirect('history')


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            author = Author.objects.get(user=request.user)
            post.author = author
            post.save()
            return redirect('post_list')
    form = PostForm()
    context = {"form": form}
    return render(request, "blog/post_create.html", context)



def login_view(request):
    if request.method == 'POST':
        password = request.POST.get("password")
        username = request.POST.get("username")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
        else:
            messages.error(request, "Incorrect Password")
    return render(request, "blog/login.html")


def logout_view(request):
    logout(request)
    return redirect('post_list')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('post_list')
        else:
            messages.error(request, 'An error occured during registration')
    form = UserForm()
    context = {'form': form}
    return render(request, "blog/signup.html", context)



def create_comment(request, pk):
    post = Post.objects.get(id=pk)
    form = CommentForm(request.POST)
    comment = form.save(commit=False)
    comment.post = post
    comment.author = request.user
    comment.save()
    comments = post.comments.all()
    context = {"comments": comments}
    return render(request, "partials/comments.html", context)


def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return HttpResponse()

def can_comment(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Login to comment"}, status=403)

def Author_profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'userprofile.html', context)


def updateUser(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = AuthorForm(request.POST, request.FILES, instance=request.user.author)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('author_profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = AuthorForm(instance=request.user.author)
    return render(request, 'update-user.html', {'user_form': user_form, 'profile_form': profile_form})
