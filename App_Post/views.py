from multiprocessing import context
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from App_Login.views import user
from .models import *
from App_Login.models import Follow
# Create your views here.
@login_required
def home(request):
    following_list=Follow.objects.filter(follower=request.user)
    posts=Post.objects.filter(author__in=following_list.values_list('following'))
    liked_post=Like.objects.filter(user=request.user)
    liked_post_list=liked_post.values_list('post',flat=True)
    if request.method=='GET':
        search=request.GET.get('search','')
        result=User.objects.filter(username__icontains=search)
    context={
        'title':'home',
        'search':search,
        'result':result,
        'following_list':following_list,
        'posts':posts,
        'liked_post_list':liked_post_list
    }
    return render(request,'APP_Post/home.html',context)

@login_required
def liked(request,pk):
    post=Post.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    if not already_liked:
        liked_post=Like(post=post,user=request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse('App_Post:home'))

@login_required
def unliked(request,pk):
    post=Post.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Post:home'))