from django.shortcuts import render, redirect
from .models import Post, User
from .forms import PostForm
from django.utils import timezone


def homepage(request):
    posts = Post.objects.all()
    return render(request, 'post/homepage.html', {'posts':posts})

def post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post/wpis.html', {'post':post})

def user(request, pk):
    user = User.objects.get(pk=pk)
    posts = user.post_set.all()
    return render(request, 'post/user.html', {'user': user, 'posts': posts})

def like(request, pk):
    post = Post.objects.get(pk=pk)
    post.like_count += 1
    post.save()
    return redirect('post:post', pk=post.pk)

def follow(request, pk):
    user = User.objects.get(pk=pk)
    user.followers_count += 1
    user.save()
    return redirect('post:user', pk=user.pk)

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.posted_date = timezone.now()
            post.who_wrote_it = User.objects.get(pk=1)
            post.save()
            return redirect('post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/new_post.html', {'form':form})

def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/new_post.html', {'form': form})

def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('homepage')