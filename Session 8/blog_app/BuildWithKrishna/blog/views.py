from django.utils import timezone
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Post
from django.db.models import Q
def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{"posts":posts})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def search(request):
    search = request.POST.get('search')
    posts = Post.objects.filter(
         Q(post_title__icontains=search) | 
         Q(post_content__icontains=search) 
    )
    return render(request,'allpost.html',{"posts":posts})

def signup(request):


    if request.method=='POST':
         username = request.POST.get('username')
         fname = request.POST.get('fname')
         pass1 = request.POST.get('pass1')
         pass2 = request.POST.get('pass2')
         email = request.POST.get('email')
         if(len(username)<8):
            messages.error(request,"Username Must be 8 characters !")
            return redirect('index')
         if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.success(request,"User Already Exist with username")
                return redirect('index')
            user = User.objects.create_user(username,email,password=pass1)
            user.first_name = fname
            user.save()
            messages.success(request,"Congratulations")
            return redirect('index')
         else:
              print("helloo")
        
    else:
        messages.success(request,"Something went Wrong!")
        return redirect('index')
    
        


def loginHandler(request):
        if request.method == 'POST':
            username = request.POST.get('loginusername')
            password = request.POST.get('loginpass')
            user = authenticate(username=username,password=password)
            if user == None:
                messages.error(request,"No User Found")
                return redirect('index')

            login(request,user)
            messages.success(request,"Login Successfull")
            return redirect('index')
        else:
            messages.error(request,"Login failed")
            return redirect('index')
             
        

def logoutHandler(request):
        logout(request)
        messages.success(request,"Logout Successfull")
        return redirect('index')

def allpost(request):
     posts = Post.objects.all()
     print(posts)
     for post in posts:
          print(post)
     return render(request,"allpost.html",{"posts":posts})

def detail(request,post_id):
     p=Post.objects.get(post_id=post_id)
     return render(request,"detail.html",{"post":p})

def createPost(request):
     return render(request,"createPost.html")

def create(request):

     title = request.POST.get('title')
     content = request.POST.get('content')
     image = request.FILES.get("thumbnail")
     time = timezone.now()
     if request.user.username=="":
          author="unknown"
     else:
          author= request.user.username;
     post = Post(post_author = author, post_title=title,post_image = image,post_time=time,post_content=content)
     post.save()
     messages.success(request,"Post Created Succesfully")
     return redirect('index')


def yourpost(request):
     posts = Post.objects.filter(post_author=request.user.username)
     for post in posts:
          print(post.post_title)
     return render(request,"yourpost.html",{"posts":posts})

def delete(request,post_id):
     post = Post.objects.filter(post_id=post_id)
     post.delete()
     messages.success(request,"Post deleted")
     return redirect('index')

def edit(request,post_id):
    post = Post.objects.get(post_id=post_id) 
    return render(request,'editpost.html',{"post":post})

def update(request,post_id):
    post = Post.objects.get(post_id=post_id)
    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.FILES.get('thumbnail')
    time = timezone.now()
    post.post_title = title
    post.post_content=content
    post.post_time = time
    if request.FILES.get("thumbnail"):
        post.post_image = image

    post.save()
    messages.success(request,"Post Updated!")
    return redirect('allpost')