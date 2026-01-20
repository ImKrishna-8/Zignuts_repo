from django.shortcuts import render,redirect
from .models import Pizza,Order,OrderItem
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import login,logout,authenticate
# Create your views here.
import json
def index(request):
    pizzas = Pizza.objects.all()
    return render(request,'index.html',{'pizzas':pizzas})

def checkout(request):
    data = json.loads(request.body)
    order = Order.objects.create(user=request.user)

    for pizzaid,item in data.items():
        pizza = Pizza.objects.get(id=pizzaid)

        order_item = OrderItem.objects.create(
            order=order,
            pizza=pizza,
            quantity=item['qty'],
            price=item['price']
        )

    return JsonResponse({'order_id': order.id})

def orderDetail(request,order_id):
    return render(request,'orderpage.html',{'order_id':order_id})

def orders(request):
     orders = Order.objects.filter(user=request.user).order_by('-created_at')
     return render(request, 'allorders.html', {'orders': orders})


def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"User Already Exist with username")
                return redirect('home')
            user = User.objects.create_user(username=username,email=email,password=pass1)
            user.first_name = fname
            user.save()
            messages.success(request,"Congratulations")
            return redirect('home')
        else:
            messages.error(request,"Password Mismatch")
            return redirect('home')
    else:
        messages.error(request,"Request Error")
        return redirect('home')


def loginHandler(request):
    loginusername = request.POST.get('loginusername')
    password = request.POST.get('loginpass')

    user = authenticate(username=loginusername,password=password)

    if user is None:
        messages.error(request,"User Not Found")
        return redirect('home')
    
    login(request,user)
    messages.success(request,"Login Successfull")
    return redirect('home')

def logoutHandler(request):
    logout(request)
    messages.success(request,"Logout Successfull")
    return redirect('home')
    
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
